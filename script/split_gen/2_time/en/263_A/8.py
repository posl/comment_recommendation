def main():
    # Read the input
    A, B, C, D, E = map(int, input().split())
    
    # Check if the condition is satisfied
    if A == B == C and D == E:
        print('Yes')
    elif A == B and C == D == E:
        print('Yes')
    else:
        print('No')
