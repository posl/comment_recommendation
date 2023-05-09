def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_p = 1000001
    for i in range(N):
        if min_p >= P[i]:
            ans += 1
            min_p = P[i]
    print(ans)

if __name__ == '__main__':
    main()