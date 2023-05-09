def main():
    N = int(input())
    A = [[1]]
    for i in range(1, N):
        A.append([1] + [A[i-1][j-1] + A[i-1][j] for j in range(1, i)] + [1])
    for a in A:
        print(*a)
