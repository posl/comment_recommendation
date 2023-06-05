def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print("黄金")
    elif A==0 and B>0:
        print("银")
    elif A>0 and B>0:
        print("合金")
    else:
        print("输入错误")
