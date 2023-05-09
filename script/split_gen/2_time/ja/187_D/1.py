def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    A.append(0)
    B.append(0)
    A_sum = [0]
    B_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    for b in B:
        B_sum.append(B_sum[-1] + b)
    ans = 10**9
    for i in range(N + 1):
        a = A_sum[i]
        b = B_sum[N] - B_sum[i]
        if a < b:
            ans = min(ans, i)
    print(ans)
