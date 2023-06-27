import sys

letters = sys.argv[1].lower()
flag = False
for line in sys.stdin:
    temp = line.strip().split(":")
    if temp[0].lower() == letters:
        print(temp[1])
        flag = True

if not flag:
    print("could not find "+letters+" in the acronym list")
        
