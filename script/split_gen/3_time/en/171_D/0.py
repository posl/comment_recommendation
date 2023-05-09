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
    S = sum(A)
    count = [0] * (10**5 + 1)
    for a in A:
        count[a] += 1
    for i in range(Q):
        S += count[B[i]] * (C[i] - B[i])
        count[C[i]] += count[B[i]]
        count[B[i]] = 0
        print(S)
