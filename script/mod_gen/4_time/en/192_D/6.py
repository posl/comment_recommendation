def solve(X, M):
    d = max(X)
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    else:
        ans = 0
        for i in range(int(d)+1, M+1):
            n = 0
            for j in range(len(X)):
                n += int(X[j]) * (i ** (len(X)-j-1))
            if n <= M:
                ans += 1
            else:
                break
        return ans
X = input()
M = int(input())
print(solve(X, M))

if __name__ == '__main__':
    solve()