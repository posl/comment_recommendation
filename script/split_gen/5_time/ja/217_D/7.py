def main():
    import sys
    readline = sys.stdin.buffer.readline
    L,Q = map(int,readline().split())
    X = [0,L]
    for _ in range(Q):
        c,x = map(int,readline().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            idx = X.index(x)
            print(X[idx+1]-X[idx-1])
