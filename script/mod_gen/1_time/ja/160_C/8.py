def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)
    ans = 10**18
    for i in range(N):
        ans = min(ans, K-(A[i+1]-A[i]))
    print(ans)
main()
