def poor(A, B, C):
    if A == B and A != C:
        return True
    elif A == C and A != B:
        return True
    elif B == C and B != A:
        return True
    else:
        return False
A, B, C = map(int, input().split())

if __name__ == '__main__':
    poor()