def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[i] = A[i]*2
    for i in range(N-1):
        ans[i+1] -= ans[i]
    print(*ans)

if __name__ == '__main__':
    main()