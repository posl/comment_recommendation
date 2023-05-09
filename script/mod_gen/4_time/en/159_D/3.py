def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for i in range(1, N+1):
        d[i] = 0
    for i in range(N):
        d[A[i]] += 1
    ans = 0
    for i in range(1, N+1):
        ans += d[i]*(d[i]-1)//2
    for i in range(N):
        print(ans-(d[A[i]]-1))

if __name__ == '__main__':
    main()