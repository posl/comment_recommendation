def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    B = [0]*(N+1)
    for i in range(1,N+1):
        B[A[i]] += 1
    ans = [0]*(N+1)
    for i in range(1,N+1):
        ans[i] = (N-1) - (B[A[i]]-1)
    for i in range(1,N+1):
        print(ans[i])

if __name__ == '__main__':
    main()