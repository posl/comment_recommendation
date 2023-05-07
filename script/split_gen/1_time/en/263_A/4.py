def main():
    # A,B,C,D,E = input().split()
    # A,B,C,D,E = int(A),int(B),int(C),int(D),int(E)
    A,B,C,D,E = map(int,input().split())
    if A == B == C and D == E and A != D and B != E and C != D:
        print('Yes')
    elif A == B == D and C == E and A != C and B != E and D != C:
        print('Yes')
    elif A == B == E and C == D and A != C and B != D and E != C:
        print('Yes')
    elif A == C == D and B == E and A != B and C != E and D != B:
        print('Yes')
    elif A == C == E and B == D and A != B and C != D and E != B:
        print('Yes')
    elif A == D == E and B == C and A != B and D != C and E != B:
        print('Yes')
    elif B == C == D and A == E and B != A and C != E and D != A:
        print('Yes')
    elif B == C == E and A == D and B != A and C != D and E != A:
        print('Yes')
    elif B == D == E and A == C and B != A and D != C and E != A:
        print('Yes')
    elif C == D == E and A == B and C != A and D != B and E != A:
        print('Yes')
    else:
        print('No')
