import subprocess
import sys


def is_in_comment(file_path, line_num, search_name):
    lines = open(file_path).readlines()

    in_comment = False
    i = 0
    for line in lines:
        i += 1
        ###   Comment Handling   ###
        if in_comment:
            if "*/" in line:
                line = line[line.index("*/")+2:]
                in_comment = False
            else:
                if i == line_num:
                    return True
                continue
        while "/*" in line and "*/" in line and (line.index("*/") > line.index("/*")):
            # remove middle comments
            line = line[:line.index("/*")] + line[line.index("*/")+2:]
        if "//" in line and ((not "/*" in line) or
                             (line.index("//") < line.index("/*"))):
            line = line[:line.index("//")]
        elif "/*" in line:
            line = line[:line.index("/*")]
            in_comment = True
        ### End Comment Handling ###
        if i == line_num:
            return not search_name in line


def get_name_before_last_outer_paren(line):
    # find index of last outer paren
    paren_depth = 0
    index_last_0_paren = 0
    for i in range(len(line)):
        c = line[i]
        if c == '(':
            if paren_depth == 0:
                index_last_0_paren = i
            paren_depth += 1
        elif c == ')':
            paren_depth -= 1
            if paren_depth < 0:
                return "<-paren>"
                print("paren depth went negative on '" + line + "'")
                exit()

    if index_last_0_paren == 0:
        return "<0paren>"
    try:
        piece = line[:index_last_0_paren].split()[-1]
    except:
        return "<bad_line>"

    if piece[0] == '*':
        return piece[1:]
    return piece

                    

def brace_depth_change_from_line(line):
    return line.count("{") - line.count("}")
def paren_depth_change_from_line(line):
    return line.count("(") - line.count(")")

def get_func_from_file_line(file_path, line_num):
    lines = open(file_path).readlines()
    
    current_func = "<None>"
    in_func = False
    in_comment = False
    brace_depth = 0
    paren_depth = 0
    func_depth = 0
    i = 0
    for line in lines:
        ###   Comment Handling   ###
        if in_comment:
            if "*/" in line:
                line = line[line.index("*/")+2:]
                in_comment = False
            else:
                i += 1
                continue
        while "/*" in line and "*/" in line and (line.index("*/") > line.index("/*")):
            # remove middle comments
            line = line[:line.index("/*")] + line[line.index("*/")+2:]
        if "//" in line and ((not "/*" in line) or
                             (line.index("//") < line.index("/*"))):
            line = line[:line.index("//")]
        elif "/*" in line:
            line = line[:line.index("/*")]
            in_comment = True
        ### End Comment Handling ###


        paren_depth += paren_depth_change_from_line(line)
        if not in_func:
            if "(" in line and (current_func == "<None>" or paren_depth == 0):
                current_func = get_name_before_last_outer_paren(line)
            if ';' in line:
                current_func = "<None>"

        brace_depth += brace_depth_change_from_line(line)
        if brace_depth == 0:
            func_depth = 0
        elif len(line.split()) >=2 and line.split()[0] == "extern" and line.split()[1] == '"C"':
            func_depth = brace_depth
        if brace_depth < 0:
            print("brace depth went negative on line " + line_num + " of file " + file_path)
        if (not in_func) and brace_depth > func_depth:
            in_func = True
        if (in_func) and brace_depth == func_depth:
            in_func = False
            current_func = "<None>"

        i += 1
        if i >= line_num:
            break
        if False and file_path == "intlib/kernelres.c" and i > line_num - 50:
            print("brace: " + str(brace_depth) + ",  curFunc: " + current_func + ",  inFunc: " + str(in_func) + ", Line: " + str(line_num))
    return current_func


def no_dec(out, search_name):
    clean = ""
    for line in out.split('\n'):
        first_raw_i = len(':'.join(line.split(' ', 1)[0].split(':')[:-1]))+1
        raw = line[first_raw_i:]
        if not search_name +'(' in ''.join(raw.split()):
            continue  # not a call; skip
        file_info = line[:first_raw_i]
        if "autoerr.h" in file_info:
            continue  # just a macro to add error checking; skip

        words = raw.split()
        good = True
        for i in range(len(words)-1):
            if words[i] == "Error" and words[i+1].startswith(search_name):
                good = False  # a declaration, not a call; skip
                break
        if good:
            clean += line+'\n'
    return clean




        
def callers_of(search_name):
    cmd = "grep -winre "+search_name
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    out, err = proc.communicate()
    out = no_dec(out[:-1], search_name).rstrip()
    grep_list = []
    for line in out.split('\n'):
        if not len(line):
            continue
        fpath = line.split(':')[0]
        if not any([ fpath.endswith(ending) for ending in [".c",".h",".cc",".cxx"]]):
            continue
        lnum = int(line.split(':')[1])
        if is_in_comment(fpath, lnum, search_name):
            continue
        if line.startswith("INTEGRITY-libs"):
            continue  # we dont care about libraries using funcs
        #print(str(lnum) + " " +fpath)
        caller = get_func_from_file_line(fpath, lnum)
        grep_list.append((caller, line))
    return grep_list


def all_callers(search_name, already_called=[], max_depth=20, ignore_externals=False, stop_on_allowed=False):
    if max_depth == 0:
        return {}
    callers_of_list = callers_of(search_name)
    already_called_new = already_called
    caller_dict = {}
    for (caller, line) in callers_of_list:
        if caller in already_called:
            continue
        already_called_new.append(caller)
        if caller in caller_dict:
            caller_dict[caller][0].append(line)
        else:
            sub_calls = {}
            if stop_on_allowed and caller in external_kcalls and external_kcalls[caller] == "A":
                sub_calls = {}
            else:
                sub_calls = all_callers(caller, already_called_new, max_depth-1, stop_on_allowed=stop_on_allowed)
            if caller in external_kcalls:
                sub_calls[".in SSM"] = external_kcalls[caller]
            caller_dict[caller] = [[line], sub_calls]
    return caller_dict
        

def print_SSM_callers_from_dict(d, indent=0):
    for k in d:
        h = d[k]
        if k == ".in SSM":
            continue
        sub_d = h[1]
        p = k
        if ".in SSM" in sub_d:
            print('|  '*indent + k + " " + sub_d[".in SSM"])
        else:
            print('|  '*indent + k)
        print_SSM_callers_from_dict(sub_d, indent+1)
        
        

def main():
    
    # handle args
    k = sys.argv[1]
    search_name = k
    recursive = False
    verbose = False
    end_with_line = False
    
    if not recursive:
        grep_list = callers_of(search_name)
        print("###   "+search_name+"   ###\n")
        for gr in grep_list:
            caller, line = gr
            print line
            print("CALLER: "+caller)
            print
            
    else:
        import json
        d = all_callers(search_name, max_depth=5, already_called=["Handler", "!defined","||"], stop_on_allowed=stop_on_allowed)
        ssm_category = ' '+external_kcalls[search_name] if search_name in external_kcalls else ''
        if verbose:
            pretty = json.dumps(d, indent=4, sort_keys=True)
            print(search_name+ssm_category+':')
            print(pretty)
        else:
            print(search_name+ssm_category+':')
            print_SSM_callers_from_dict(d, indent=1)
    if end_with_line:
        print '_'*70
        


if __name__ == "__main__":
    main()
