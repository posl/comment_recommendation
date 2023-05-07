def main():
    #入力
    N = int(input())
    #処理
    ans = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    #出力
    print(ans)
