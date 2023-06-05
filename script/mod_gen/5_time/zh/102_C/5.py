def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [A[i]-(i+1) for i in range(N)]
    A.sort()
    if N%2 == 0:
        b = (A[N//2-1]+A[N//2])//2
    else:
        b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i]-b)
    print(ans)

if __name__ == '__main__':
    main()