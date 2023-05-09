def main():
    X, N = map(int, input().split())
    P = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    P = list(set(P))
    P.sort()
    if X <= P[0]:
        print(P[0])
        return
    if X >= P[-1]:
        print(P[-1])
        return
    for i in range(N):
        if X <= P[i]:
            if X - P[i-1] <= P[i] - X:
                print(P[i-1])
                return
            else:
                print(P[i])
                return
main()

if __name__ == '__main__':
    main()