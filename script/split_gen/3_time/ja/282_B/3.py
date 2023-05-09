def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if 'o' * m == ''.join([s[i][k] if s[i][k] == 'o' else s[j][k] for k in range(m)]):
                ans += 1
    print(ans)
