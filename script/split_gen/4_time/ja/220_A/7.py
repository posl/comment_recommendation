def main():
    # A,B,Cの値を受け取る
    a,b,c = map(int, input().split())
    # A以上B以下のCの倍数を求める
    if a % c == 0:
        print(a)
    else:
        print((a // c + 1) * c)
