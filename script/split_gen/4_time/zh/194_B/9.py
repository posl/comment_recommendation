def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min([max(A[i], B[j]) for i in range(N) for j in range(N)]))
