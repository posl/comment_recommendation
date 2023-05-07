def main():
    #入力
    P = list(map(int,input().split()))
    
    #出力
    print("".join([chr(ord("a")+i-1) for i in P]))
