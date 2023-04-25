Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2] == 'R':
        print(3)
    elif s[0] == s[1] == 'R' or s[1] == s[2] == 'R':
        print(2)
    elif s[0] == 'R' or s[1] == 'R' or s[2] == 'R':
        print(1)
    else:
        print(0)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    max_count = 0
    for i in S:
        if i == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 3

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == "R":
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 5

def main():
    weather = input()
    rainy_days = 0
    max_rainy_days = 0
    for day in weather:
        if day == "R":
            rainy_days += 1
        else:
            rainy_days = 0
        if rainy_days > max_rainy_days:
            max_rainy_days = rainy_days
    print(max_rainy_days)

=======
Suggestion 6

def max_rainy_days(s):
    rainy_days = 0
    max_rainy_days = 0
    for i in range(len(s)):
        if s[i] == "R":
            rainy_days += 1
        else:
            rainy_days = 0
        if rainy_days > max_rainy_days:
            max_rainy_days = rainy_days
    return max_rainy_days

=======
Suggestion 7

def max_rainy_days(s):
    max_rainy_days = 0
    rainy_days = 0
    for i in range(len(s)):
        if s[i] == 'R':
            rainy_days += 1
        else:
            if rainy_days > max_rainy_days:
                max_rainy_days = rainy_days
            rainy_days = 0
    if rainy_days > max_rainy_days:
        max_rainy_days = rainy_days
    return max_rainy_days

=======
Suggestion 8

def main():
    S = input()
    print(S.count('R'))

=======
Suggestion 9

def main():
    # Take input from stdin
    S = input()
    # Create a list from the input
    S = list(S)
    # Initialize counter
    counter = 0
    # Initialize max counter
    max_counter = 0
    # Iterate over the list
    for i in S:
        # If the character is R
        if i == 'R':
            # Increment the counter
            counter += 1
            # If the counter is greater than the max counter
            if counter > max_counter:
                # Set the max counter to the counter
                max_counter = counter
        # If the character is S
        else:
            # Reset the counter
            counter = 0
    # Print the max counter
    print(max_counter)
