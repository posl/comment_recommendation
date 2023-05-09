def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    B = [a % M for a in A]
    from collections import Counter
    C = Counter(B)
    ans = 0
    for k, v in C.items():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()