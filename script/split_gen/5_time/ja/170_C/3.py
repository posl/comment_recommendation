def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(1, X + 1):
        if not i in p:
            print(i)
            return
    for i in range(X, 0, -1):
        if not i in p:
            print(i)
            return
