def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    B = [0] * (T + 1)
    for a, b in AB:
        B[a] += 1
        B[b] -= 1
    for i in range(1, T + 1):
        B[i] += B[i - 1]
    A = [0] * (T + 1)
    for i in range(1, T + 1):
        A[i] = A[i - 1] + (B[i] == 0)
    ans = 'Yes'
    for a, b in AB:
        if A[b] - A[a] == 0:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()