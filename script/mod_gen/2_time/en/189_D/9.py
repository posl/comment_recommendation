def solve(n,s):
    ans = 0
    for i in range(2**n):
        x = [int(j) for j in list('{:0{}b}'.format(i,n))]
        y = x[0]
        for j in range(1,n):
            if s[j-1] == 'AND':
                y = y and x[j]
            else:
                y = y or x[j]
        if y:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()