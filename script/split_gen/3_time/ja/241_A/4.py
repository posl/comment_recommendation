def main():
    #入力
    a = list(map(int, input().split()))
    #処理
    ans = 0
    for i in range(3):
        ans = a[ans]
    #出力
    print(ans)
