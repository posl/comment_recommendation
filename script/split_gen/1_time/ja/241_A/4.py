def main():
    #入力
    a = list(map(int,input().split()))
    #処理
    for i in range(3):
        a0 = a[0]
        for j in range(9):
            a[j] = a[j+1]
        a[9] = a0
    #出力
    print(a[0])
    return
