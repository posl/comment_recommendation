Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)

=======
Suggestion 2

def main():
    n = int(input())
    if 1 <= n <= 125:
        print(4)
    elif 126 <= n <= 211:
        print(6)
    else:
        print(8)

=======
Suggestion 3

def problems214_a():
    n = int(input())
    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)

=======
Suggestion 4

def abc_problem(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8

=======
Suggestion 5

def problem214_a():
    # Store the number of problems in each ABC
    problems_in_ABC = [4, 6, 8]
    # Get the input
    N = int(input())
    # Calculate the number of problems in the N-th ABC
    if N <= 125:
        num_of_problems = problems_in_ABC[0]
    elif N <= 211:
        num_of_problems = problems_in_ABC[1]
    else:
        num_of_problems = problems_in_ABC[2]
    # Output the result
    print(num_of_problems)
    return
