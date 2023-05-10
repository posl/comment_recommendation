def main():
    n = int(input())
    w = [input() for _ in range(n)]
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            print('No')
            exit()
        if w.count(w[i]) > 1:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()