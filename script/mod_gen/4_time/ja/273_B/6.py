def solve():
    X,K = map(int,input().split())
    for i in range(K):
        if X % 10 != 0:
            X += 5 - (X % 10) if X % 10 < 5 else 10 - (X % 10)
        else:
            X //= 10
    print(X)

if __name__ == '__main__':
    solve()