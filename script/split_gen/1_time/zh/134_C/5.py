def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max1 = max(A)
    for i in range(N):
        if A[i] == max1:
            A.pop(i)
            break
    for i in range(N-1):
        print(max(A))
