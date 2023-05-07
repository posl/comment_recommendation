def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = "Yes"
    now = N
    for i in range(M):
        if i == 0:
            now -= A[i]
        else:
            now -= A[i] - B[i - 1]
        if now <= 0:
            ans = "No"
            break
        now += B[i] - A[i]
        if now > N:
            now = N
    if ans == "Yes":
        now -= T - B[M - 1]
        if now <= 0:
            ans = "No"
    print(ans)

if __name__ == '__main__':
    main()