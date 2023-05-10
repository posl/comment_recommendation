def solve():
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ab = sorted(zip(a, b))
    ab.reverse()
    ab_i = 0
    ab_sum = 0
    m_sum = 0
    for m_i in range(m):
        while ab_i < n and ab[ab_i][0] <= m_i + 1:
            ab_sum += ab[ab_i][1]
            ab_i += 1
        m_sum += ab_sum
    return m_sum
print(solve())
