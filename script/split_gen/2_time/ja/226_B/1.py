def main():
    N = int(input())
    d = {}
    for i in range(N):
        L = list(map(int, input().split()))
        L = tuple(L[1:])
        if L in d:
            d[L] += 1
        else:
            d[L] = 1
    print(len(d))
