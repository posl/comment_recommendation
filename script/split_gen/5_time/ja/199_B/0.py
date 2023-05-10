def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        for j in range(N):
            if A[j] <= i <= B[j]:
                if j == N-1:
                    ans += 1
            else:
                break
    print(ans)
