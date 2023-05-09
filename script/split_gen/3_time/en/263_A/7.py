def main():
    # Read the input
    A, B, C, D, E = map(int, input().split())
    # Check the conditions
    if (A == B == C and D == E and A != D) or (A == B and C == D == E and A != C):
        print('Yes')
    else:
        print('No')
