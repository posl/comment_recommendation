def solve():
    n = int(input())
    s = input()
    l = 0
    r = 0
    ans = [0]
    for i in range(n):
        if s[i] == 'L':
            l += 1
            ans.insert(r, i + 1)
        else:
            r += 1
            ans.append(i + 1)
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    solve()