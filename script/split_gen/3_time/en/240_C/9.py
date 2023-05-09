def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = "No"
    for i in range(2**N):
        s = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j][1]
            else:
                s += A[j][0]
        if s == X:
            ans = "Yes"
    print(ans)
