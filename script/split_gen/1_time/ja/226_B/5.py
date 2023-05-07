def main():
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]
    d = {}
    for i in range(N):
        L = A[i][0]
        a = tuple(A[i][1:])
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    print(len(d))
