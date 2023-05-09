def main():
    #input
    X, K, D = map(int, input().split())
    #compute
    X = abs(X)
    if K*D <= X:
        ans = X - K*D
    else:
        K -= X//D
        X = X%D
        if K%2 == 1:
            ans = abs(X-D)
        else:
            ans = X
    #output
    print(ans)

if __name__ == '__main__':
    main()