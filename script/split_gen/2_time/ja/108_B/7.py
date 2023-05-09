def main():
    #入力
    x1,y1,x2,y2=map(int,input().split())
    
    #出力
    print(x2-y2+y1,y2+x2-x1,x1-y2+y1,y1+x2-x1)
