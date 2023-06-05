def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        words.append(word)
        if i == 0:
            continue
        if words[i][0] != words[i-1][-1]:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()