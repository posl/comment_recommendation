def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    elif C == A and C != B:
        print("Yes")
    else:
        print("No")
    return
