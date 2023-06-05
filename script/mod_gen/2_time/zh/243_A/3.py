def solve():
    s = input()
    q = int(input())
    tks = []
    for _ in range(q):
        tk = input().split()
        tk[0] = int(tk[0])
        tk[1] = int(tk[1])
        tks.append(tk)
    for tk in tks:
        t = tk[0]
        k = tk[1]
        for i in range(t):
            s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
        print(s[k - 1])

if __name__ == '__main__':
    solve()