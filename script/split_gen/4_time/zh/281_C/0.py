def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    T %= sum(A)
    a = 0
    for i in range(N):
        T -= A[i]
        if T < 0:
            a = i
            break
    print(a+1, T+A[a])
