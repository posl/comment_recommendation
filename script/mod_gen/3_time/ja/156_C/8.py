def main():
    N = int(input())
    X = list(map(int, input().split()))
    #print(N)
    #print(X)
    #X.sort()
    #print(X)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans += (X[i] - X[j]) ** 2
    print(ans)

if __name__ == '__main__':
    main()