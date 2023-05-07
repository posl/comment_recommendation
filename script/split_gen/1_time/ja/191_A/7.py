def main():
    #入力
    V,T,S,D = map(int,input().split())
    #出力
    if V*T <= D <= V*S:
        print("No")
    else:
        print("Yes")
