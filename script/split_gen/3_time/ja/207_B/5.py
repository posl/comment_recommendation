def main():
    A,B,C,D = map(int,input().split())
    if A > B * D:
        print(-1)
    elif A <= B:
        print(0)
    else:
        print((A - B + B * D - 1) // (B * D - B) + 1)
