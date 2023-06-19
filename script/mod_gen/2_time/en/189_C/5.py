def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for x in range(1, 10**5+1):
        tmp = 0
        for i in range(N):
            if A[i] >= x:
                tmp += 1
            else:
                ans = max(ans, tmp*x)
                tmp = 0
        ans = max(ans, tmp*x)
    print(ans)
main()
