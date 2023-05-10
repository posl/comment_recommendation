def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    if N == 0:
        print(X)
        exit()
    p = sorted(p)
    if X not in p:
        print(X)
        exit()
    for i in range(1, 100):
        if X - i not in p:
            print(X-i)
            exit()
        elif X + i not in p:
            print(X+i)
            exit()
    print(0)
