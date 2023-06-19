def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    words_set = set(words)
    if len(words_set) != n:
        print("No")
        return
    for i in range(1, n):
        if words[i-1][-1] != words[i][0]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()