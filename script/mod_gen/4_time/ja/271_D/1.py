def solve():
    N, S = map(int, input().split())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))
    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if (i & (1 << j)) != 0:
                sum += A[j][0]
            else:
                sum += A[j][1]
        if sum == S:
            print("Yes")
            for j in range(N):
                if (i & (1 << j)) != 0:
                    print("H", end="")
                else:
                    print("T", end="")
            print()
            return
    print("No")

if __name__ == '__main__':
    solve()