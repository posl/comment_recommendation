def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(0)
    for i in range(N):
        ans[A[i] - 1] += 1
    for i in range(N):
        print(ans[i])
