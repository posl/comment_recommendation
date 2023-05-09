def main():
    N = int(input())
    S = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        a = (S[i] - 3) // 4
        b = (S[i] - 3) % 4
        if a > 0 and b == 0 and S[i] == (4*a*a + 3*a + 3):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()