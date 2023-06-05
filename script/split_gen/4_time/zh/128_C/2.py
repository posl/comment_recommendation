def main():
    N,M = map(int,input().split())
    k = []
    for i in range(M):
        k.append(list(map(int,input().split())))
    p = list(map(int,input().split()))
    count = 0
    for i in range(2**N):
        on = 0
        for j in range(M):
            s = 0
            for l in range(k[j][0]):
                if i >> (k[j][l+1]-1) & 1:
                    s += 1
            if s % 2 == p[j]:
                on += 1
        if on == M:
            count += 1
    print(count)
