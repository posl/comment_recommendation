def main():
    import sys
    from collections import Counter
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [Counter(A[i][1:]) for i in range(M)]
    C = Counter()
    for i in range(M):
        for j in B[i]:
            C[j] += B[i][j]
    for i in C:
        if C[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()