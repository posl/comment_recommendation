def main():
    N,A,B = map(int,input().split())
    b = N//(A+B)
    r = N%(A+B)
    print(b*A+r if r<=A else b*A+A)
