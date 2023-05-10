def problems115_b():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[N-1] = p[N-1]//2
    print(sum(p))
