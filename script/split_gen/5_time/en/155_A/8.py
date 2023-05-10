def main():
    # Get input here
    A, B, C = map(int, input().strip().split())
    # Calculate result here
    if A == B and B == C:
        print("No")
    elif A == B or B == C or A == C:
        print("Yes")
    else:
        print("No")
main()
