def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * N
    for i in range(M):
        if A[i] == 1:
            ans[B[i]-1] = A[i]
        elif B[i] == 1:
            ans[A[i]-1] = B[i]
    for i in range(M):
        if ans[A[i]-1] == 0:
            ans[A[i]-1] = B[i]
        elif ans[B[i]-1] == 0:
            ans[B[i]-1] = A[i]
    for i in range(N):
        if ans[i] == 0:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(ans[i])
main()

if __name__ == '__main__':
    main()