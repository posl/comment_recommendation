def solve(n, a, b, p, q, r, s):
    #print("n=%d, a=%d, b=%d, p=%d, q=%d, r=%d, s=%d" % (n, a, b, p, q, r, s))
    ret = []
    for i in range(p, q+1):
        ret.append([])
        for j in range(r, s+1):
            ret[i-p].append('.')
    for k in range(max(1-a, 1-b), min(n-a, n-b)+1):
        ret[a+k-p][b+k-r] = '#'
    for k in range(max(1-a, b-n), min(n-a, b-1)+1):
        ret[a+k-p][b-k-r] = '#'
    for k in range(max(a-n, 1-b), min(a-1, n-b)+1):
        ret[a-k-p][b+k-r] = '#'
    for k in range(max(a-n, b-n), min(a-1, b-1)+1):
        ret[a-k-p][b-k-r] = '#'
    for i in range(q-p+1):
        print(''.join(ret[i]))

if __name__ == '__main__':
    solve()