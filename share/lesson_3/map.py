import sys
import re

def main():
    for line in sys.stdin:
        words = re.findall(r'\w+', line)
        for word in words:
            print(word, '\t1')

if __name__ == '__main__':
    main()