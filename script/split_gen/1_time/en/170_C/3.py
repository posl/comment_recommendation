def main():
    X, N = map(int, input().split())
    p = set(map(int, input().split()))
    for i in range(100):
        if X - i not in p:
            print(X - i)
            break
        if X + i not in p:
            print(X + i)
            break
