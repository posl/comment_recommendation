def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        B = []
        for j in range(0, len(A), 2):
            if A[j] > A[j + 1]:
                B.append(A[j])
            else:
                B.append(A[j + 1])
        A = B
    print(A[0])
