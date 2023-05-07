def solve():
    s = input()
    n = len(s)
    a = 0
    for i in range(n):
        if int(s[i]) == (i % 2):
            a += 1
    print(min(a, n - a))

if __name__ == '__main__':
    solve()