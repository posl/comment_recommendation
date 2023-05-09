def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2])
    P = P[::-1]
    s = sum(P[K - 1])
    for i in range(N):
        if sum(P[i]) >= s:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()