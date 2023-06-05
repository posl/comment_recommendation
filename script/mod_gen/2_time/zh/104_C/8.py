def get_problem_num(problem_list, score, bonus):
    if score >= bonus:
        return 0
    else:
        return 1

if __name__ == '__main__':
    get_problem_num()