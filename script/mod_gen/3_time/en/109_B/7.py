def main():
    #input
    N = int(input())
    W = [input() for _ in range(N)]
    #compute
    for i in range(1, N):
        if W[i-1][-1] != W[i][0] or W[i] in W[:i]:
            print('No')
            return
    #output
    print('Yes')

if __name__ == '__main__':
    main()