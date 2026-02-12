import sys

def main():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        word, count = line.strip().split("\t")
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word is not None:
                print(current_word, current_count)
            current_word = word
            current_count = count

    if current_word is not None:
        print(current_word, current_count)

if __name__ == '__main__':
    main()