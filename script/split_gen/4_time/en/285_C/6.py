def get_problem_number(problem_id):
    problem_number = 0
    problem_id = problem_id[::-1]
    for i in range(len(problem_id)):
        problem_number += (ord(problem_id[i]) - 64) * (26**i)
    return problem_number
