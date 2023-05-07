def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(N - 1 - i):
            if B[j] > B[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                B[j], B[j + 1] = B[j + 1], B[j]
    time = 0
    for i in range(N):
        time += A[i]
        if time > B[i]:
            print("No")
            return
    print("Yes")
