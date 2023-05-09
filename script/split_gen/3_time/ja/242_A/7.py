def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X <= B:
        print((B-X+1)/B)
    else:
        print(0)
