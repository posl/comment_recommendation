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
    if X >= p[-1]:
        print(p[-1])
        return
    for i in range(N-1):
        if p[i] <= X <= p[i+1]:
            if X - p[i] <= p[i+1] - X:
                print(p[i])
            else:
                print(p[i+1])
            return
