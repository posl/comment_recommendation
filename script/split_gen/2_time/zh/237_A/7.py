def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 2**N):
        x = []
        for j in range(N):
            if (i >> j) & 1:
                x.append(j)
        if len(x) == 1:
            continue
        for j in range(len(x)):
            for k in range(j+1, len(x)):
                ans ^= A[x[j]][x[k]]
    print(ans)
