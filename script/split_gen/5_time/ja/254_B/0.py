def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([1]*(i+1))
    for i in range(2,N):
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(" ".join(map(str,A[i])))
