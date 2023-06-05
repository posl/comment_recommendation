def main():
    A,B,C = map(int,input().split())
    if A > C:
        print(0)
    else:
        print(B//A)
