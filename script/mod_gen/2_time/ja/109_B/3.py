def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(W) != len(set(W)):
        print('No')
        return
    for i in range(1, len(W)):
        if W[i][0] != W[i-1][-1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()