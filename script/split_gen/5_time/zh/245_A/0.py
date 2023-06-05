def main():
    A,B,C,D = map(int, input().split())
    if A > C:
        print("高桥")
    elif A == C and B > D:
        print("高桥")
    else:
        print("青木")
