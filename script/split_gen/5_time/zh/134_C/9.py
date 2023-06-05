def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    max = max(A)
    for i in range(N):
        if A[i] == max:
            print(max(A[:i]+A[i+1:]))
        else:
            print(max)
