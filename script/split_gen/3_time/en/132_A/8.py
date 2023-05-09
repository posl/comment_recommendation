def main():
    # Read the input.
    s = input()
    # Count the number of each character.
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    # Check the number of each character.
    # If the number of each character is 2, print Yes.
    # Otherwise, print No.
    if len(count) == 2 and 2 in count.values():
        print("Yes")
    else:
        print("No")
