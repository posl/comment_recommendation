def main():
    n, m = map(int, input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        a, b = input().split()
        a = int(a)
        if s[a-1] == 0 and b == 'AC':
            s[a-1] = 1
        elif b == 'WA' and s[a-1] == 0:
            p[a-1] += 1
    print(sum(s), sum([s[i]*p[i] for i in range(n)]))
    return
