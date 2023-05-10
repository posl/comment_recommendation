def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        p = P[i]
        if p == 1:
            ans += 1
            break
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()