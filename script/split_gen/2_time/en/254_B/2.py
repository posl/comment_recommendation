def main():
    N = int(input())
    A = [[1], [1, 1]]
    for i in range(2, N):
        A.append([1])
        for j in range(1, i):
            A[i].append(A[i-1][j-1] + A[i-1][j])
        A[i].append(1)
    for i in range(N):
        print(" ".join(map(str, A[i])))
