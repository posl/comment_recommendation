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
    count_B = [0] * 10**5
    for a in A:
        count_B[a-1] += 1
    for i in range(Q):
        sum_A += count_B[B[i]-1] * (C[i] - B[i])
        count_B[C[i]-1] += count_B[B[i]-1]
        count_B[B[i]-1] = 0
        print(sum_A)
