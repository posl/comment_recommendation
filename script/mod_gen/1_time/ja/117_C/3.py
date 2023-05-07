def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        exit()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    ans = 0
    for i in range(M-N):
        ans += diff[i]
    print(ans)

if __name__ == '__main__':
    main()