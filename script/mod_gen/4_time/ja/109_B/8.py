def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                pass
            else:
                if words[i] == words[j]:
                    print("No")
                    exit()
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()