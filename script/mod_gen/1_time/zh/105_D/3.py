def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    A = [a % M for a in A]
    from collections import Counter
    C = Counter(A)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()