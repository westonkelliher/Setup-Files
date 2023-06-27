#!/usr/bin/python
import sys

def count_text_chars(s):
    num = 0
    for c in s:
        if (c.isalnum() or c.isspace() or c in
            '~!@#$%^&*()_+`-=[]\{}|;\':",./<>?'):
            num += 1
    return num

def is_file_text():
    filename = sys.argv[1]
    f = open(filename)
    filestr = f.read()
    f.close()
    if len(filestr) > 1000:
        filestr = filestr[:1000]
    elif len(filestr) == 0:
        return False
    text_ratio = (0.0 + count_text_chars(filestr))/len(filestr)
    return text_ratio > .9


if __name__ == '__main__':
    exit(is_file_text())
