def main():
    # Take input from stdin
    a, b = map(int, input().split())
    # Check for the conditions
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Alloy")
