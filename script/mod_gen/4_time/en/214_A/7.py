def get_problem_count():
    problem_count = 0
    n = int(input("Enter the number of ABC contests: "))
    if n >= 1 and n <= 125:
        problem_count = 4
    elif n >= 126 and n <= 211:
        problem_count = 6
    elif n >= 212 and n <= 214:
        problem_count = 8
    return problem_count
print(get_problem_count())
