def main():
    N, M = map(int, input().split())
    p = [0] * M
    y = [0] * M
    for i in range(M):
        p[i], y[i] = map(int, input().split())
    for i in range(M):
        print('{:06}{:06}'.format(p[i], y.index(y[i]) + 1))
