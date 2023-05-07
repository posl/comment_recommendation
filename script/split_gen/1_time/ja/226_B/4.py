def main():
    N = int(input())
    d = dict()
    for i in range(N):
        L = list(map(int, input().split()))
        L = tuple(L[1:])
        d[L] = d.get(L, 0) + 1
    print(len(d))
