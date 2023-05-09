def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    minP = P[0]
    for i in range(N):
        if minP >= P[i]:
            ans += 1
            minP = P[i]
    print(ans)

if __name__ == '__main__':
    main()