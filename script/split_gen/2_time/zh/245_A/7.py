def main():
    A,B,C,D = map(int, input().split())
    if (A > C) or (A == C and B > D):
        print("高桥")
    else:
        print("青木")
