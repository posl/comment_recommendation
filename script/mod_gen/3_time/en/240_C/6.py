def main():
    N, X = map(int, input().split())
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    
    for i in range(N):
        X -= min(X, a[i])
        X -= min(X, b[i])
    
    if X == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()