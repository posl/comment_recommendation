def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    c = Counter(A)
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if c[A[j]] > 1 or A[i] + A[j] > A[j+1]:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()