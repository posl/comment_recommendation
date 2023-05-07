def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                ans += A[i][j]
            else:
                ans -= A[i][j]
    print(ans)
