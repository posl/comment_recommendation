def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1
    for i in range(n):
        if s[i] == 'AND':
            ans *= 2
        else:
            ans = ans * 2 + 2 ** (i + 1)
    print(ans)
main()
