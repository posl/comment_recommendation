def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = A[::-1]
    B = B[::-1]
    count = 0
    for i in range(N):
        if (A[i] + count) % B[i] != 0:
            count += B[i] - (A[i] + count) % B[i]
    print(count)
