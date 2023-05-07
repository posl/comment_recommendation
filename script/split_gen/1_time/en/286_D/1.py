def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    if total >= X:
        print("Yes")
    else:
        print("No")
