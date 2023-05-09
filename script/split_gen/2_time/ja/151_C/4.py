def main():
    N, M = map(int, input().split())
    d = {}
    for i in range(1, N+1):
        d[i] = [0, 0]
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            d[p][0] = 1
        else:
            if d[p][0] == 0:
                d[p][1] += 1
    print(sum([d[i][0] for i in d]), sum([d[i][1] for i in d if d[i][0] == 1]))
