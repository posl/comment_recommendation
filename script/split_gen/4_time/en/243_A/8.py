def main():
    V,A,B,C = map(int,input().split())
    if A + B + C <= V:
        print("M")
    elif A + B <= V:
        print("T")
    elif A <= V:
        print("F")
    else:
        print("M")
