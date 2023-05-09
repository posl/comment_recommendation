def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A == A[::-1]:
        print(0)
        return
    M = max(A)
    B = [0] * (M + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for b in B:
        ans += b // 2
    print(N - ans * 2)

if __name__ == '__main__':
    main()