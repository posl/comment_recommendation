def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        if P[i] > P[i-K]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()