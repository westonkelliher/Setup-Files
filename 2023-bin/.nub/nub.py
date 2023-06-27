import sys
from termcolor import colored
from os import path

NUBLIST = []
HIER = {}
CURRENT = 0
NOTES = []

def father(nub):
    return HIER[nub][0]

def nubstr(nub):
    return NUBLIST[nub-1] + '\n'
def nubstr_fmt(nub):
    if NOTES[nub-1]:
        return colored(NUBLIST[nub-1], 'white', attrs=['dark'])
    return colored(NUBLIST[nub-1], 'yellow')


def assert_size(args, n):
    if len(args) > n:
        print("too many arguments")
        exit(1)
    elif len(args) < n:
        print("missing argument")
        exit(1)

def command(cmd):
    global CURRENT

    # current-branch
    if (not len(cmd)) or cmd[0] == '':
        print(current_branch())

    # add-adjacent
    elif cmd[0] == 'a':
        assert_size(cmd, 2)
        addNub(father(CURRENT), ' '.join(cmd[1:]))
        CURRENT = len(NUBLIST)

    # add-sub
    elif cmd[0] == 's':
        assert_size(cmd, 2)
        addNub(CURRENT, ' '.join(cmd[1:]))
        CURRENT = len(NUBLIST)

    # list
    elif cmd[0] == 'l':
        nub = CURRENT
        x = '0'
        if cmd[1]:
            assert_size(cmd, 2)
            x = cmd[1]
            if x.startswith('-'): # relative
                n = int(x[1:])
                for i in range(n):
                    nub = father(nub)
            else:
                print("not impl")
                exit(1)
        for subnub in HIER[nub][1:]:
            sys.stdout.write(nubstr_fmt(subnub))

                
    # tree
    elif cmd[0] == 't':
        noop = 5



def addNub(father, nubstr):
    NUBLIST.append(nubstr + '\n')
    nub = len(NUBLIST)
    HIER.append([father])
    HIER[father].append(nub)


# TODO:
# current_branch gets a list of nodes in incresing level order
# print_branch prints the nubs in order with color and indentation
def current_branch():
    return ''.join(_current_branch(CURRENT))
def _current_branch(nub):
    #print(nub)
    f = father(nub)
    if f == 0:
        return [nubstr_fmt(nub)]
    pre = _current_branch(f)
    #print(pre)
    pre.append("  "*len(pre) + nubstr_fmt(nub))
    return pre


def hierString(hier, current):
    wstr = str(current)+'\n'
    for key in hier:
        wstr += key + ':'
        for n in hier[key]:
            wstr += n+','
        wstr += '\n'
    return wstr
        


def main():
    global NUBLIST, HIER, CURRENT, COLORS, NOTES
    nubdir=sys.argv[1]
    nublist_f = open(nubdir+"/nublist", "a+")
    nubhier_f = open(nubdir+"/nubhier", "a+")
    NUBLIST = nublist_f.readlines()
    NOTES = [nubdir+'/'+str(n+1)+".txt" if
             path.exists(nubdir+'/'+str(n+1)+".txt") else None
             for n in range(len(NUBLIST))]
    nubhier = nubhier_f.readlines()
    HIER = [[int(y) for y in x.split()] for x in nubhier]
    CURRENT = HIER[0][0]
    cmd = sys.argv[2:]
    command(cmd)

    nublist_f.seek(0)
    nublist_f.truncate()
    nublist_f.writelines(NUBLIST)
    HIER[0][0] = CURRENT
    nubhier = [" ".join([str(x) for x in y])+'\n' for y in HIER]
    nubhier_f.seek(0)
    nubhier_f.truncate()
    nubhier_f.writelines(nubhier)

main()


def print_colors():
    for x in ['red', 'blue', 'green', 'yellow', 'cyan',
              'magenta', 'grey', 'white']:
        a = colored('@', x)
        b = colored('@', x, attrs=['bold'])
        c = colored('@', x, attrs=['dark'])
        d = colored('@', x, attrs=['bold', 'dark'])
        print(a + " " + b + " " + c + " " + d + "\n")
