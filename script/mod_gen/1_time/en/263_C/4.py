def seq(n, m, s):
    if n == 0:
        print(' '.join(map(str, s)))
        return
    for i in range(1, m + 1):
        if not s or i > s[-1]:
            s.append(i)
            seq(n - 1, m, s)
            s.pop()
n, m = map(int, input().split())
seq(n, m, [])

if __name__ == '__main__':
    seq()