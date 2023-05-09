def main():
    A,B,C,X = map(int,input().split())
    if A<=X<=B:
        print((C/(B-A+1)))
    else:
        print(0)
