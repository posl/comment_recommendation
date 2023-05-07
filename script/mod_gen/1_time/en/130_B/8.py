def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        if ans + L[i] > X:
            break
        ans += L[i]
    print(ans)

if __name__ == '__main__':
    main()