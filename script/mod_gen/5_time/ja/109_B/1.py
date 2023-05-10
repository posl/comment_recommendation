def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        if i != 0:
            if words[i] in words[:i]:
                print('No')
                exit()
            if words[i][0] != words[i-1][-1]:
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()