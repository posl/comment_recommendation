def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in s:
        for j in t:
            if i[-3:] == j:
                ans += 1
    print(ans)
