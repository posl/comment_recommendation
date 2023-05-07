def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(input())
    A = []
    for i in range(K):
        A.append(input().split())
    d = [int(i) for i in d]
    A = [[int(j) for j in i] for i in A]
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] -= 1
    a = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            a.append(A[i][j])
    a = list(set(a))
    print(N - len(a))
