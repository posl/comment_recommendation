def main():
    N = int(input())
    ans = 10**10
    for _ in range(N):
        A, P, X = map(int, input().split())
        if A < X:
            ans = min(ans, P)
    if ans == 10**10:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()