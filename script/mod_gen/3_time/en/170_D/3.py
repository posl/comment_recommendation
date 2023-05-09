def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                ans += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                ans += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()