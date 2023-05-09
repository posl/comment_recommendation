def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)
    #print(a)
    #print(b)
    dp = [0] * (X + 1)
    dp[0] = 1
    for i in range(1, X + 1):
        for j in range(N):
            if i - a[j] >= 0 and dp[i - a[j]] == 1:
                dp[i] = 1
            elif i - b[j] >= 0 and dp[i - b[j]] == 1:
                dp[i] = 1
    #print(dp)
    print("Yes" if dp[X] == 1 else "No")

if __name__ == '__main__':
    main()