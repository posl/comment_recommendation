def main():
    n, m = map(int, input().split())
    s = [input()[-3:] for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in s:
        if i in t:
            ans += 1
    print(ans)
