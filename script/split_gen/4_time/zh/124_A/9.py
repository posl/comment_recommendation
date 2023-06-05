def main():
    A,B = map(int,input().split())
    if A == B:
        print(A*2)
    elif A > B:
        print(A+A-1)
    else:
        print(B+B-1)
