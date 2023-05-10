def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print("No")
            exit(0)
        if i != 0:
            if word[0] != prev_word[-1]:
                print("No")
                exit(0)
        words.append(word)
        prev_word = word
    print("Yes")

if __name__ == '__main__':
    main()