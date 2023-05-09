def main():
    #input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [0] * N
    Ys = [0] * N
    for i in range(N):
        Xs[i], Ys[i] = map(int, input().split())
    #calc
    def dist(x1, y1, x2, y2):
        return (x1-x2)**2 + (y1-y2)**2
    def check(R):
        for i in range(K):
            for j in range(i+1, K):
                if dist(Xs[As[i]-1], Ys[As[i]-1], Xs[As[j]-1], Ys[As[j]-1]) < R**2:
                    return False
        return True
    #output
    l = 0
    r = 10**10
    while r - l > 10**-5:
        m = (l + r) / 2
        if check(m):
            r = m
        else:
            l = m
    print(l)
