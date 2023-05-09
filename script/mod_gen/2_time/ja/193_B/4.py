def main():
    N = int(input())
    ans = 10**9+1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X-A > 0:
            ans = min(ans, P)
    if ans == 10**9+1:
        print(-1)
    else:
        print(ans)
main()

if __name__ == '__main__':
    main()