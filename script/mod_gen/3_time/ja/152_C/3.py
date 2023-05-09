def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_P = P[0]
    for i in range(1, N):
        if min_P >= P[i]:
            ans += 1
        min_P = min(min_P, P[i])
    print(ans+1)

if __name__ == '__main__':
    main()