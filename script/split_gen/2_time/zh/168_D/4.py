def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print("Yes")
    for i in range(1, N):
        print(A[B.index(i+1)])
