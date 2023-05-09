def main():
    N = int(input())
    W = [input() for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if W[i] == W[j]:
                print('No')
                return
    for i in range(1,N):
        if W[i-1][-1] != W[i][0]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()