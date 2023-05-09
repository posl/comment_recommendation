def main():
    X, N = map(int, input().split())
    if N > 0:
        p = list(map(int, input().split()))
        p.sort()
        if X <= p[0]:
            print(p[0] - 1)
        elif X >= p[-1]:
            print(p[-1] + 1)
        else:
            for i in range(N - 1):
                if p[i] < X < p[i + 1]:
                    if abs(X - p[i]) > abs(X - p[i + 1]):
                        print(p[i + 1])
                    else:
                        print(p[i])
                    break
    else:
        print(X)
