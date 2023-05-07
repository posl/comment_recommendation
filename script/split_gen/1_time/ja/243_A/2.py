def main():
    V,A,B,C = map(int,input().split())
    if A > V:
        print("F")
    elif A+B > V:
        print("M")
    elif A+B+C > V:
        print("T")
    else:
        print("F")
