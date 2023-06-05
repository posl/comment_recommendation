def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[0] = 0
        elif a[i] == a[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + 1
    for i in range(n):
        print(ans[i])
