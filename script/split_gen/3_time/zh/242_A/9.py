def main():
    A,B,C,X = map(int, input().split())
    if A >= X:
        print(1.0)
    elif A < X <= B:
        print(1/C)
    else:
        print(0.0)
