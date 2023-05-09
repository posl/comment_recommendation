def main():
    A,B,C,D,E = map(int,input().split())
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and B == D and C == E:
        print("Yes")
    elif A == B and B == E and C == D:
        print("Yes")
    elif A == C and C == D and B == E:
        print("Yes")
    elif A == C and C == E and B == D:
        print("Yes")
    elif A == D and D == E and B == C:
        print("Yes")
    elif B == C and C == D and A == E:
        print("Yes")
    elif B == C and C == E and A == D:
        print("Yes")
    elif B == D and D == E and A == C:
        print("Yes")
    elif C == D and D == E and A == B:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()