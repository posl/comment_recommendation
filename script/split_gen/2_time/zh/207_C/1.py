def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i][1] <= A[j][2] and A[j][1] <= A[i][2]:
                ans += 1
    print(ans)
