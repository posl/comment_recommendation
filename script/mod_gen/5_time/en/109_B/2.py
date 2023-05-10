def main():
    N = int(input())
    W = [input() for i in range(N)]
    for i in range(1, N):
        if W[i] in W[:i] or W[i][0] != W[i-1][-1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()