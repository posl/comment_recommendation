def main():
    # Read input from stdin
    A,B,C,D,E = map(int,input().split())
    # Check if the set is a Full house
    if A == B == C and D == E:
        print("Yes")
    elif A == B and C == D == E:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()