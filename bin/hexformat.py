import sys

MAX_LINE_LEN = 64
if len(sys.argv) == 3:
    MAX_LINE_LEN = int(sys.argv[2])

file_path = sys.argv[1]

f = open(file_path)

hex_chars = []
ascii_chars = []

for line in f:
    for i in range(8):
        start = i*5 + 10
        hex_chars.append(line[start:start+2])
        hex_chars.append(line[start+2:start+4])
    for c in line[51:-1]:
        ascii_chars.append(c)

for h in range(8):
    if hex_chars[-1] == '  ':
        hex_chars.pop()
    else:
        break


hex_line = ""
ascii_line = ""
line_len = 0
for i in range(len(hex_chars)):
    hex_line += hex_chars[i] + ""
    if hex_chars[i] == '0a':
        ascii_line += "LF"
        print(hex_line)
        print(ascii_line)
        print("")
        print("")
        print("")
        hex_line = ""
        ascii_line = ""
        line_len = 0
    elif hex_chars[i] == '0d':
        ascii_line += "CR"
    else:
        ascii_line += ascii_chars[i] + " "
        
    if line_len == MAX_LINE_LEN:
        print(hex_line)
        print(ascii_line)
        print("")
        hex_line = ""
        ascii_line = ""
        line_len = 0
    else:
        line_len += 1
