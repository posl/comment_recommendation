def main():
    n = int(input())
    w = [input() for i in range(n)]
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print('No')
            return
        for j in range(i+1,n):
            if w[i] == w[j]:
                print('No')
                return
    print('Yes')
    return

if __name__ == '__main__':
    main()