def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*n
    # aの中の数字の個数をカウント
    cnt = [0]*n
    for i in range(n):
        cnt[a[i]-1] += 1
    # 重複組み合わせの計算
    for i in range(n):
        ans[i] = cnt[a[i]-1]*(cnt[a[i]-1]-1)//2
    # 重複組み合わせを引く
    for i in range(n):
        print(n*(n-1)//2-ans[i])
