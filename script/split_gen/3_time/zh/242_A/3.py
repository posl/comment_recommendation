def main():
    A,B,C,X = map(int,input().split())
    if A >= X:
        print(1)
    elif A < X and X <= B:
        print(C/(B-A))
    else:
        print(0)
