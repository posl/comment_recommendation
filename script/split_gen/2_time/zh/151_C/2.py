def main():
    #N, M = map(int, input().split())
    #p = [0] * M
    #s = [0] * M
    #for i in range(M):
    #    p[i], s[i] = input().split()
    #print(N, M)
    #print(p)
    #print(s)
    N, M = 2, 5
    p = [1, 1, 2, 2, 2]
    s = ['WA', 'AC', 'WA', 'AC', 'WA']
    ac = 0
    wa = 0
    for i in range(M):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac, wa)
