def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print("No")
            return
        else:
            words.append(word)
        if i > 0 and words[i-1][-1] != words[i][0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()