def main():
    D, G = map(int, input().split())
    problems = []
    for i in range(D):
        problems.append(list(map(int, input().split())))
    min_num = 100000
    for i in range(2 ** D):
        score = 0
        num = 0
        for j in range(D):
            if ((i >> j) & 1):
                score += (j + 1) * 100 * problems[j][0] + problems[j][1]
                num += problems[j][0]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D - 1, -1, -1):
                if ((i >> j) & 1) == 0:
                    for k in range(problems[j][0]):
                        if score >= G:
                            break
                        score += (j + 1) * 100
                        num += 1
            if score >= G:
                min_num = min(min_num, num)
    print(min_num)

if __name__ == '__main__':
    main()