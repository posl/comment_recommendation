def main():
    N = int(input())
    A = list(map(int, input().split()))
    # x = (A[0] + A[1] - A[N - 1]) // 2
    # print(x)
    x = (A[0] + A[1] - A[N - 1]) // 2
    ans = [x]
    for i in range(1, N):
        x = A[i - 1] - x
        ans.append(x)
    print(" ".join(map(str, ans)))
