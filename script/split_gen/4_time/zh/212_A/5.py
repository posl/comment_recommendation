def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print("黄金")
    elif A==0 and B>0:
        print("银")
    else:
        print("合金")
