def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if a[i] == a[i - 1]:
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] + 1
    for i in range(N - 1, 0, -1):
        if a[i] == a[i - 1]:
            ans[i - 1] = ans[i]
    print('\n'.join(map(str, ans)))
