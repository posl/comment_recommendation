def main():
    X, N = map(int, input().split())
    p = set(map(int, input().split()))
    for i in range(101):
        if not X - i in p:
            print(X - i)
            break
        if not X + i in p:
            print(X + i)
            break
