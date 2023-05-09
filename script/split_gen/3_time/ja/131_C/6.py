def main():
    A,B,C,D=map(int,input().split())
    C1=B//C
    D1=B//D
    C2=(A-1)//C
    D2=(A-1)//D
    LCM=C*D//math.gcd(C,D)
    LCM1=B//LCM
    LCM2=(A-1)//LCM
    print(B-A+1-(C1-D1+LCM1)-(C2-D2+LCM2))
