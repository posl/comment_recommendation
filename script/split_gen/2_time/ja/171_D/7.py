def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [tuple(map(int, input().split())) for _ in range(Q)]
    ans = [0] * Q
    ans[0] = sum(A)
    B = [0] * (10 ** 5 + 1)
    for a in A:
        B[a] += 1
    for i in range(1, Q):
        b, c = BC[i]
        ans[i] = ans[i - 1] - b * B[b] + c * B[b]
        B[c] += B[b]
        B[b] = 0
    for a in ans:
        print(a)
