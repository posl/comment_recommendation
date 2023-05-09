def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    if X not in p:
        print(X)
        return
    p.sort()
    for i in range(1, 101):
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return
