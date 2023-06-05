def solve():
    n = int(input())
    s = input()
    ans = []
    for i in range(1,n):
        l = 0
        while i+l < n and s[l] != s[i+l]:
            l += 1
        ans.append(l)
    print('\n'.join(map(str,ans)))

if __name__ == '__main__':
    solve()