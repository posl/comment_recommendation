def main():
    A,B,C,X = map(int,input().split())
    if A >= X:
        print(1)
    elif A < X and B >= X:
        print(C/(B-A))
    else:
        print(0)
