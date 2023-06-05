def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    t = 0
    for i in range(N):
        if t < A[i]:
            t = A[i]
        if t % B[i] != 0:
            t += B[i] - t % B[i]
    print(t)
