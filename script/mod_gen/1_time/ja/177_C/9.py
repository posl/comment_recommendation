def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    A.sort()
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += (A[i] * A[j])
    print(sum % mod)
main()
