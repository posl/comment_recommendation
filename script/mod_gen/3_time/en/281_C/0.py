def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    T %= total
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i+1, -T)
            return
main()
