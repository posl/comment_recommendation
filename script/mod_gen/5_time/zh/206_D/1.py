def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    l = 0
    r = N-1
    while l<r:
        if A[l] == A[l+1]:
            l += 2
        else:
            l += 1
        if A[r] == A[r-1]:
            r -= 2
        else:
            r -= 1
        ans += 1
    if l == r:
        ans += 1
    print(ans)
main()
