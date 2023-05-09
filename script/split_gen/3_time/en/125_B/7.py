def main():
    # input
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # compute
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    # output
    print(ans)
