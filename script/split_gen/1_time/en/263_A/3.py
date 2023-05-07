def main():
    A,B,C,D,E = map(int,input().split())
    if A == B == C and D != E:
        print('Yes')
    elif D == E == C and A != B:
        print('Yes')
    elif A == B == D and C != E:
        print('Yes')
    elif A == B == E and C != D:
        print('Yes')
    elif A == C == D and B != E:
        print('Yes')
    elif A == C == E and B != D:
        print('Yes')
    elif A == D == E and B != C:
        print('Yes')
    elif B == C == D and A != E:
        print('Yes')
    elif B == C == E and A != D:
        print('Yes')
    elif B == D == E and A != C:
        print('Yes')
    elif C == D == E and A != B:
        print('Yes')
    else:
        print('No')
