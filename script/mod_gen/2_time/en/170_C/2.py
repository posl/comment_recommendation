def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    if X <= p[0]:
        print(p[0])
        return
    elif p[-1] <= X:
        print(p[-1])
        return
    for i in range(1, N):
        if p[i - 1] < X and X < p[i]:
            if X - p[i - 1] <= p[i] - X:
                print(p[i - 1])
            else:
                print(p[i])
            return
main()

if __name__ == '__main__':
    main()