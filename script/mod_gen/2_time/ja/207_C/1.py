def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][0] == 1:
                l1 = A[i][1]
            elif A[i][0] == 2:
                l1 = A[i][1] + 1
            elif A[i][0] == 3:
                l1 = A[i][1]
            else:
                l1 = A[i][1] + 1
            if A[j][0] == 1:
                l2 = A[j][1]
            elif A[j][0] == 2:
                l2 = A[j][1] + 1
            elif A[j][0] == 3:
                l2 = A[j][1]
            else:
                l2 = A[j][1] + 1
            if A[i][0] == 1:
                r1 = A[i][2]
            elif A[i][0] == 2:
                r1 = A[i][2]
            elif A[i][0] == 3:
                r1 = A[i][2] - 1
            else:
                r1 = A[i][2] - 1
            if A[j][0] == 1:
                r2 = A[j][2]
            elif A[j][0] == 2:
                r2 = A[j][2]
            elif A[j][0] == 3:
                r2 = A[j][2] - 1
            else:
                r2 = A[j][2] - 1
            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()