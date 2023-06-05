def solve():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            if s[i+1] == 'R':
                j = i
                while s[j] != 'L':
                    ans[j] += 1
                    j += 1
                if (j-i) % 2 == 1:
                    ans[j] += 1
            else:
                j = i
                while s[j] != 'L':
                    ans[j] += 1
                    j += 1
        else:
            if s[i-1] == 'L':
                j = i
                while s[j] != 'R':
                    ans[j] += 1
                    j -= 1
                if (i-j) % 2 == 1:
                    ans[j] += 1
            else:
                j = i
                while s[j] != 'R':
                    ans[j] += 1
                    j -= 1
    print(' '.join(map(str, ans)))
solve()
