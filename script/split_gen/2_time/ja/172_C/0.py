def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0]
    B_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    for b in B:
        B_sum.append(B_sum[-1] + b)
    ans = 0
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        ans = max(ans, i + (M - (len(B_sum) - bisect.bisect_right(B_sum, K - A_sum[i]))) + 1)
    print(ans)
