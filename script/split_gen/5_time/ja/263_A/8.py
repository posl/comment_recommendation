def main():
    A,B,C,D,E = map(int,input().split())
    if A == B and C == D and D == E:
        print("No")
    elif A == B and B == C and D == E:
        print("Yes")
    elif A == B and B == C and C == D:
        print("Yes")
    else:
        print("No")
