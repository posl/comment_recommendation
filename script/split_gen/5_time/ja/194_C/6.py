def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        for j in range(0, i):
            ans += (A[i] - A[j]) ** 2
    print(ans)
