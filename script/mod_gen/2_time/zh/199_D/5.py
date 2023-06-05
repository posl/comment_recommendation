def solve():
    n = int(input())
    s = input()
    q = int(input())
    # 0-indexed
    # 前半部分
    s1 = s[:n]
    # 后半部分
    s2 = s[n:]
    # 1-indexed
    # 前半部分
    s1 = list(s1)
    # 后半部分
    s2 = list(s2)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            if a < n and b < n:
                s1[a], s1[b] = s1[b], s1[a]
            elif a < n and b >= n:
                b -= n
                s1[a], s2[b] = s2[b], s1[a]
            elif a >= n and b >= n:
                a -= n
                b -= n
                s2[a], s2[b] = s2[b], s2[a]
        elif t == 2:
            s1, s2 = s2, s1
    print(''.join(s1) + ''.join(s2))

if __name__ == '__main__':
    solve()