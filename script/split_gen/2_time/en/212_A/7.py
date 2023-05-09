def main():
    # read the input
    A, B = map(int, input().split())
    # determine the output
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")
