def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    ans = [0] * n
    for i in range(n):
        cnt[a[i]-1] += 1
    for i in range(n):
        ans[i] = cnt[i] * (cnt[i]-1) // 2
    sum_ans = sum(ans)
    for i in range(n):
        print(sum_ans - ans[a[i]-1] + (cnt[a[i]-1]-1) * (cnt[a[i]-1]-2) // 2)
