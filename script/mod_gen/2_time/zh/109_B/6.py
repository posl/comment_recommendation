def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i] in words[0:i]:
            print("No")
            return
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()