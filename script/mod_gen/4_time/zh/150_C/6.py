def solve(n,p,q):
    l = []
    for i in range(n):
        l.append(i+1)
    p_index = 0
    q_index = 0
    for i in range(n):
        p_index += (l.index(p[i])) * (n-i-1)
        l.remove(p[i])
        q_index += (l.index(q[i])) * (n-i-1)
        l.remove(q[i])
    return abs(p_index - q_index)

if __name__ == '__main__':
    solve()