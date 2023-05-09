def main():
    # Read input
    A, B, C, D, E = map(int, input().split())
    # Check if the set is a Full house
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and C == D and D == E:
        print("Yes")
    else:
        print("No")
