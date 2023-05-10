def solve():
    n = input()
    ans = 0
    for i in range(1,len(n)):
        a = int(n[:i])
        b = int(n[i:])
        ans = max(ans, a*b)
    print(ans)

if __name__ == '__main__':
    solve()