def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = []
    for i in range(N):
        if A[i] != X:
            A_.append(A[i])
    for i in range(len(A_)):
        if i == len(A_)-1:
            print(A_[i])
        else:
            print(A_[i], end=" ")
