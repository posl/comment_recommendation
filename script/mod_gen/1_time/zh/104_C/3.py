def get_min_num_of_problems():
    D, G = map(int, input().split())
    p_c = [list(map(int, input().split())) for i in range(D)]
    min_num_of_problems = 1000
    for i in range(2 ** D):
        num_of_problems = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                num_of_problems += p_c[j][0]
                score += 100 * (j + 1) * p_c[j][0] + p_c[j][1]
        if score >= G:
            min_num_of_problems = min(min_num_of_problems, num_of_problems)
            continue
        for j in range(D - 1, -1, -1):
            if i >> j & 1:
                continue
            for k in range(p_c[j][0]):
                if score >= G:
                    break
                num_of_problems += 1
                score += 100 * (j + 1)
        min_num_of_problems = min(min_num_of_problems, num_of_problems)
    return min_num_of_problems

if __name__ == '__main__':
    get_min_num_of_problems()