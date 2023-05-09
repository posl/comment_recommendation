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

if __name__ == '__main__':
    problem214_a()