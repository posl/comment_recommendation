def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max = max(A)
    for i in range(N):
        if A[i] == max:
            A[i] = 0
            print(max(A))
            A[i] = max
