def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(1, N+1):
        ans = [0] * (N+1)
        for j in range(M):
            if A[j] == i:
                ans[B[j]] += 1
            elif B[j] == i:
                ans[A[j]] += 1
        print(sum(ans), end="")
        for j in range(1, N+1):
            if ans[j] == 1:
                print(" " + str(j), end="")
        print()

if __name__ == '__main__':
    main()