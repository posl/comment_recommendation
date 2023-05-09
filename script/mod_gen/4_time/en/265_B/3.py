def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i],Y[i] = map(int,input().split())
    time = T
    room = 1
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            return False
        if room in X:
            time += Y[X.index(room)]
            if time > T:
                time = T
        room += 1
    return True if time - A[N-2] > 0 else False
print('Yes' if solve() else 'No')

if __name__ == '__main__':
    solve()