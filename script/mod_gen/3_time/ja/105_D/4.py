def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
        A[i] %= M
    A = sorted(A)
    cnt = 0
    now = 0
    for i in range(1, N + 1):
        if A[i] == A[i - 1]:
            now += 1
        else:
            cnt += now * (now + 1) // 2
            now = 0
    cnt += now * (now + 1) // 2
    print(cnt)

if __name__ == '__main__':
    main()