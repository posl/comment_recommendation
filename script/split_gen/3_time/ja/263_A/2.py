def main():
    A,B,C,D,E = map(int,input().split())
    if A == B == C:
        if D == E:
            print("Yes")
        else:
            print("No")
    elif A == B == D:
        if C == E:
            print("Yes")
        else:
            print("No")
    elif A == B == E:
        if C == D:
            print("Yes")
        else:
            print("No")
    elif A == C == D:
        if B == E:
            print("Yes")
        else:
            print("No")
    elif A == C == E:
        if B == D:
            print("Yes")
        else:
            print("No")
    elif A == D == E:
        if B == C:
            print("Yes")
        else:
            print("No")
    elif B == C == D:
        if A == E:
            print("Yes")
        else:
            print("No")
    elif B == C == E:
        if A == D:
            print("Yes")
        else:
            print("No")
    elif B == D == E:
        if A == C:
            print("Yes")
        else:
            print("No")
    elif C == D == E:
        if A == B:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
