def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if a[i] == a[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = 1
    for i in range(N):
        if ans[i] % 2 == 0:
            print(0)
        else:
            print(1)
