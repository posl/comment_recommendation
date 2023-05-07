def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    for i in range(101):
        if (X - i) not in p:
            print(X - i)
            return
        if (X + i) not in p:
            print(X + i)
            return
