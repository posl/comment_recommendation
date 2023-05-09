def main():
    N, K = map(int, input().split())
    P = [0] * N
    for i in range(N):
        P[i] = sum(map(int, input().split()))
    P.sort(reverse=True)
    if P[K - 1] < P[K]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()