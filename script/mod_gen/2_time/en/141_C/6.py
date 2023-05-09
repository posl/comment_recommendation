def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    for i in range(1, N+1):
        if K - (Q - A.count(i)) > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()