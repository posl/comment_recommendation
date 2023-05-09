def main():
    N = int(input())
    ans = -1
    for _ in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            if ans == -1:
                ans = P
            else:
                ans = min(ans, P)
    print(ans)

if __name__ == '__main__':
    main()