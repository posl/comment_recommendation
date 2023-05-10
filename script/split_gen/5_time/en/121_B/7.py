def main():
    # input
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    # compute
    ans = 0
    for a in A:
        if sum([a[i]*B[i] for i in range(M)]) + C > 0:
            ans += 1
    # output
    print(ans)
