def main():
    N, M = list(map(int, input().strip().split(' ')))
    problem_dict = {}
    for i in range(M):
        p, S = input().strip().split(' ')
        if p not in problem_dict:
            problem_dict[p] = [S]
        else:
            problem_dict[p].append(S)
    AC_count = 0
    WA_count = 0
    for k, v in problem_dict.items():
        if 'AC' in v:
            AC_count += 1
            WA_count += v.index('AC')
    print(AC_count, WA_count)

if __name__ == '__main__':
    main()