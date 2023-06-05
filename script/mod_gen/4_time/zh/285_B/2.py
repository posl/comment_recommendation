def solve():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while l + i < n and s[l] != s[l + i]:
            l += 1
        print(l)

if __name__ == '__main__':
    solve()