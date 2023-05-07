def main():
    N = int(input())
    W = [input() for i in range(N)]
    for i in range(N-1):
        if W[i][-1] != W[i+1][0] or W[i] in W[i+1:]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()