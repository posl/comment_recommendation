def main():
    A, B, C, X = map(int, input().split())
    if X >= A:
        if X <= B:
            print(1)
        else:
            print(0)
    else:
        print((C)/(B-A+1))
