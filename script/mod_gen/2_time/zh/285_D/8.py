def get_index_of_problem(problem_id):
    index = 0
    for i in range(len(problem_id)):
        index += (ord(problem_id[i]) - ord('A') + 1) * 26 ** (len(problem_id) - 1 - i)
    return index

if __name__ == '__main__':
    get_index_of_problem()