def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(W) != len(set(W)):
        print('No')
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print('No')
            return
    print('Yes')
main()

if __name__ == '__main__':
    main()