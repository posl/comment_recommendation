def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(1,N):
        if A[i-1] != A[i]:
            ans += i
    print(ans)

if __name__ == '__main__':
    main()