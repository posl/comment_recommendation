def main():
    # Read the input
    A, B = map(int, input().split())
    # Check the conditions
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")
main()

if __name__ == '__main__':
    main()