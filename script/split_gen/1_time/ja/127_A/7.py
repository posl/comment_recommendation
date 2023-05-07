def main():
    #入力
    A,B = map(int,input().split())
    #出力
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(B//2)
    else:
        print(0)
