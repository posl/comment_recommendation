def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    ans = [0]*(2*n+1)
    for i in range(1, n+1):
        ans[i] = ans[a[i]] + 1
        ans[i*2] = ans[i]
        ans[i*2+1] = ans[i]
    for i in range(1, 2*n+1):
        print(ans[i])
