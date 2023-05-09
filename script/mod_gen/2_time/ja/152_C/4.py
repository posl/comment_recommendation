def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    minP = 10 ** 9 + 1
    for i in range(N):
        if P[i] <= minP:
            ans += 1
            minP = P[i]
    print(ans)

if __name__ == '__main__':
    main()