def main():
    X, K = map(int, input().split())
    #print(X, K)
    #print(X % 10**K)
    #print(X % 10**K >= 5 * 10**(K-1))
    if X % 10**K >= 5 * 10**(K-1):
        print(X + 10**K - X % 10**K)
    else:
        print(X - X % 10**K)
    return
