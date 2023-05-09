def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    p.sort()
    #print(p)
    if X <= p[0]:
        print(p[0])
        return
    if X >= p[-1]:
        print(p[-1] + 1)
        return
    for i in range(len(p) - 1):
        if p[i] < X and p[i + 1] > X:
            if X - p[i] == p[i + 1] - X:
                print(p[i])
                return
            if X - p[i] < p[i + 1] - X:
                print(p[i])
                return
            else:
                print(p[i + 1])
                return
main()
