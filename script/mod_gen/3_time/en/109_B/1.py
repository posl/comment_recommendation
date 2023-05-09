def main():
    n = int(input())
    w = [input() for _ in range(n)]
    for i in range(1, n):
        if w[i] in w[:i] or w[i-1][-1] != w[i][0]:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()