def main():
    N, M = map(int, input().split())
    problems = []
    for i in range(M):
        problems.append(list(input().split()))
    problems = sorted(problems, key=lambda x: int(x[0]))
    correct = 0
    penalty = 0
    for i in range(M):
        if problems[i][1] == "AC":
            correct += 1
            for j in range(i, M):
                if problems[i][0] == problems[j][0]:
                    if problems[j][1] == "WA":
                        penalty += 1
                    else:
                        break
    print(correct, penalty)

if __name__ == '__main__':
    main()