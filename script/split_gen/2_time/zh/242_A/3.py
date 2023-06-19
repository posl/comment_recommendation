def main():
    A,B,C,X = map(int,input().split())
    if A>X:
        print(0)
    elif B>=X>=A:
        print(1)
    else:
        print(C/(B-A))
