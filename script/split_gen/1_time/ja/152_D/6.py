def main():
    #入力
    N = int(input())
    
    #初期化
    ans = 0
    cnt = [0]*10
    cnt2 = [0]*10
    for i in range(1,N+1):
        cnt[i%10] += 1
        cnt2[i//10] += 1
    for i in range(10):
        ans += cnt[i] * cnt2[i]
    print(ans)
