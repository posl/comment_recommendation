def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        ans = max(ans, min(s.count(s[j][i]) for j in range(n)))
    print(n * 10 - ans)
