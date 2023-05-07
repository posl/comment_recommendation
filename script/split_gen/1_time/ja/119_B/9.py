def main():
    N = int(input())
    
    #合計金額の初期化
    total = 0
    
    #N人分の入力を受け取る
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        if u == "BTC":
            total += x * 380000.0
    
    #出力
    print(total)
