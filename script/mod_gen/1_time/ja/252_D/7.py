def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    N = int(input())
    A = list(map(int,input().split()))
    C = Counter(A)
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if A[i] != A[j]:
                ans += N - j - 1 - C[A[i]] - C[A[j]]
                C[A[i]] -= 1
    print(ans)

if __name__ == '__main__':
    main()