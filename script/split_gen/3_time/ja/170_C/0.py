def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        p = list(map(int, input().split()))
        if X not in p:
            print(X)
        else:
            for i in range(0, 101):
                if X - i not in p:
                    print(X - i)
                    break
                if X + i not in p:
                    print(X + i)
                    break
