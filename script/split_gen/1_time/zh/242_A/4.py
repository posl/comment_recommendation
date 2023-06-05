def main():
    A,B,C,X = [int(x) for x in input().split()]
    if X <= A:
        print(1)
    elif X > B:
        print(0)
    else:
        print(C/(B-A))
