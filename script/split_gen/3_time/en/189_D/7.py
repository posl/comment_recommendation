def main():
    n = int(input())
    s = [input() for i in range(n)]
    ans = 1
    for i in range(n):
        if s[i] == 'AND':
            ans = 2 * ans
        else:
            ans = 2 * ans + 1
    print(ans)
