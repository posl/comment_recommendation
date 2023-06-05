def get_problem_count(num):
    if num < 126:
        return 4
    elif num < 212:
        return 6
    else:
        return 8

if __name__ == '__main__':
    get_problem_count()