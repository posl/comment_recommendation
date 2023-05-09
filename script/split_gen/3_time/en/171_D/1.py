def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sum_A = sum(A)
    count_B = [0] * (10 ** 5 + 1)
    for a in A:
        count_B[a] += 1
    for i in range(Q):
        b = B[i]
        c = C[i]
        sum_A += count_B[b] * (c - b)
        count_B[c] += count_B[b]
        count_B[b] = 0
        print(sum_A)
