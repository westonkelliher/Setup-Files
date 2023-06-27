import random
import sys

def is_word_valid(word, in_letters, min_length=3):
    letters = (in_letters + ['.'])[:-1] # copy
    if len(word) < min_length:
        return False
    w_list = [c for c in word]
    while len(w_list):
        if not len(letters):
            return False
        if w_list[0] in letters:
            letters.remove(w_list[0])
            w_list = w_list[1:]
        else:
            return False
    return True

def get_valid_words(letters, min_length=3):
    words = open('/etc/dictionaries-common/words').read().split()
    valid_words = []
    for w in words:
        if is_word_valid(w, letters, min_length):
            valid_words.append(w)
    return valid_words

def main():
    letters = [c for c in sys.argv[1]]
    min_length = 3
    if len(sys.argv) > 2:
        min_length = int(sys.argv[2])
    words = get_valid_words(letters, min_length)
    random.shuffle(words)
    for w in words:
        print(w)

if __name__ == '__main__':
    main()
