def main():
    N = int(input())
    ans = 10**9
    for _ in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            ans = min(ans, P)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()