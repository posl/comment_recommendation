def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    if T <= sum(A):
        for i in range(N):
            if T <= A[i]:
                print(i+1, T)
                break
            else:
                T -= A[i]
    else:
        T %= sum(A)
        for i in range(N):
            if T <= A[i]:
                print(i+1, T)
                break
            else:
                T -= A[i]
