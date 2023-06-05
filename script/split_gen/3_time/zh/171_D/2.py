def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    BC = [[int(x) for x in input().split()] for _ in range(Q)]
    A_sum = sum(A)
    B_sum = [0] * (10 ** 5 + 1)
    for a in A:
        B_sum[a] += 1
    for b, c in BC:
        A_sum += (c - b) * B_sum[b]
        B_sum[c] += B_sum[b]
        B_sum[b] = 0
        print(A_sum)
