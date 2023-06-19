def solve(n, k, s):
    #print(n, k, s)
    if k >= n:
        return n
    else:
        l = 0
        r = 0
        cnt = 0
        for i in range(n):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if i > 0 and s[i] != s[i-1]:
                cnt += 1
        #print(l, r, cnt)
        if cnt <= k:
            return n
        else:
            if s[0] == 'L':
                s = 'R' + s
            else:
                s = 'L' + s
            if s[-1] == 'L':
                s = s + 'R'
            else:
                s = s + 'L'
            #print(s)
            s = list(s)
            for i in range(n+1):
                if s[i] == 'L':
                    l -= 1
                else:
                    r -= 1
                if s[i+1] == 'L':
                    l += 1
                else:
                    r += 1
                if l == r:
                    #print(l, r, i)
                    if i+1 <= k:
                        return n
                    else:
                        return n - 1
            return n

if __name__ == '__main__':
    solve()