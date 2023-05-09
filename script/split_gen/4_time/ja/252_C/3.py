def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        ans += 10
        for j in range(10):
            if s[i][j] == str(j):
                ans -= 1
                break
    print(ans)
