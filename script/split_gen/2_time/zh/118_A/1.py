def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    K = bin(K)[2:]
    K = '0' * (len(A) - len(K)) + K
    ans = 0
    for i in range(len(A)):
        if K[i] == '1':
            ans += A[i]
        else:
            ans += A[i] // 2
    print(ans)
main()
