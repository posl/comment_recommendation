def main():
    N, M = map(int, input().split())
    p = [0] * M
    s = [0] * M
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * N
    wa = [0] * N
    for i in range(M):
        if s[i] == 'AC':
            ac[p[i]-1] = 1
        elif ac[p[i]-1] == 0:
            wa[p[i]-1] += 1
    print(sum(ac), sum([ac[i]*wa[i] for i in range(N)]))
