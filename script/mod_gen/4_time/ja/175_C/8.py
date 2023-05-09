def solve():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X//D >= K:
        return X-K*D
    else:
        K -= X//D
        X -= (X//D)*D
        if K%2 == 0:
            return X
        else:
            return D-X

if __name__ == '__main__':
    solve()