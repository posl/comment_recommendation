def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(sum(map(int, input().split())))
    P.sort(reverse=True)
    print('Yes' if P[K-1] > 0 else 'No')

if __name__ == '__main__':
    main()