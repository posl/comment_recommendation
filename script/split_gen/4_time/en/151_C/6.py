def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i])
    p = p[:m]
    s = s[:m]
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
            p[i] = 0
        else:
            p[i] -= 1
    for i in range(m):
        if p[i] != 0:
            wa += 1
    print(ac,wa)
