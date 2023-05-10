def problem257_a():
    # Get input
    n, x = map(int, input().split())
    # Get the first part of the string
    first_part = x // n
    # Get the second part of the string
    second_part = x % n
    # Get the character
    character = chr(65 + second_part - 1)
    # Print the character
    print(character)
