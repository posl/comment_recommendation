def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1
    for i in range(n):
        if s[i] == 'AND':
            ans *= 2
    ans = 2 ** n - ans
    print(ans)
