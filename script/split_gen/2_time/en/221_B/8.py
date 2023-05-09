def main():
    # Read the input
    s = input()
    t = input()
    # Check if the strings are already equal
    if s == t:
        print("Yes")
        return
    # Check if it is possible to make s and t equal by swapping two adjacent characters
    for i in range(len(s) - 1):
        if s[:i] + s[i + 1] + s[i] + s[i + 2:] == t:
            print("Yes")
            return
    print("No")
