def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    i = 0
    for b in B:
        while i+1 < n and A[i] < b:
            i += 1
        ans = min(ans, abs(A[i]-b))
    print(ans)

if __name__ == '__main__':
    main()