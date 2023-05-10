def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i]) - 1
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == 'AC':
            ac[p[i]] = 1
        if s[i] == 'WA' and ac[p[i]] == 0:
            wa[p[i]] += 1
    print(sum(ac),sum([ac[i]*wa[i] for i in range(n)]))
