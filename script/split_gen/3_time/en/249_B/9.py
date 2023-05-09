def main():
    # Read the input string
    s = input()
    # Check if the string is wonderful
    if (s.islower() or s.isupper() or s.isnumeric() or len(s) < 2 or len(s) > 100):
        print("No")
    else:
        # Create a set from the string
        s_set = set(s)
        # Check if the set has the same length as the string
        if (len(s_set) == len(s)):
            print("Yes")
        else:
            print("No")
