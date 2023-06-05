def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i] - (i+1)
    B.sort()
    b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

if __name__ == '__main__':
    main()