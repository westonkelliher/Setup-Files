#!/usr/bin/python3
import sys
# takes path of .map as first argument and 


def my_filter(x):
    if '.last_d' in x:
        return False
    if x == '':
        return False
    return True

def load_map(path):
    lines = open(path).read().split('\n')
    m = {line.split(':')[0]:line.split(':')[1] for line in
         filter(lambda x: x != '', lines)}
    return m

def load_map_inverse(path):
    lines = open(path).read().split('\n')
    m = {line.split(':')[1]:line.split(':')[0] for line in
         filter(my_filter, lines)}
    return m

def save_map(path, the_map):
    f = open(path, 'w')
    keys = list(the_map.keys())
    keys.sort()
    for k in keys:
        f.write(k+':'+the_map[k]+'\n')
    f.close()

def map_add(path, key, val):
    if val[-1] == '/':
        val = val[:-1]
    m = load_map(path)
    m[key] = val
    save_map(path, m)

def map_get_val(path, key):
    m = load_map(path)
    if not key in m.keys():
        sys.stderr.write(key+' not in map\n')
        exit(5)
    return m[key]

def map_get_key(path, val):
    if val[-1] == '/':
        val = val[:-1]
    m = load_map_inverse(path)
    if not val in m.keys():
        exit(0)
    return m[val]
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('needs <subcmd> and <map_path>\n')
        exit(1)

    subcmd        = sys.argv[1]
    map_file_path = sys.argv[2]

    if subcmd == 'add':
        if not len(sys.argv) == 5:
            sys.stderr.write('not enough args\n')
            exit(3)
        map_key  = sys.argv[3]
        dir_path = sys.argv[4]
        map_add(map_file_path, map_key, dir_path)
        
    elif subcmd == 'get_dir':
        if not len(sys.argv) == 4:
            sys.stderr.write('not enough args\n')
            exit(3)
        map_key = sys.argv[3]
        print(map_get_val(map_file_path, map_key))

    elif subcmd == 'get_name':
        if not len(sys.argv) == 4:
            sys.stderr.write('not enough args\n')
            exit(3)
        map_val = sys.argv[3]
        print(map_get_key(map_file_path, map_val))

    elif subcmd == 'keys':
        for k in load_map(map_file_path).keys():
            print(k)

    else:
        sys.stderr.write("invalid subcommand: "+subcmd+'\n')    
        exit(2)
