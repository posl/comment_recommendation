def solve():
    X,K = map(int,input().split())
    for i in range(K):
        if i == K-1:
            break
        if X % (10**(K-i)) >= 5*(10**(K-i-1)):
            X = X + (10**(K-i)) - (X % (10**(K-i)))
        else:
            X = X - (X % (10**(K-i)))
    print(X)
    return 0

if __name__ == '__main__':
    solve()