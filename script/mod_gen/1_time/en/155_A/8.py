def poor(A,B,C):
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        return "Yes"
    else:
        return "No"
A,B,C = map(int,input().split())
print(poor(A,B,C))
