def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_P = N + 1
    for i in range(N):
        if P[i] < min_P:
            ans += 1
        min_P = min(min_P, P[i])
    print(ans)

if __name__ == '__main__':
    main()