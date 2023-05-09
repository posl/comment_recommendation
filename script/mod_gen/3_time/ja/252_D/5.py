def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i] and A[i]+A[j] > A[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()