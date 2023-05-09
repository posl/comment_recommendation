def main():
    N, M = map(int, input().split())
    problems = [0] * N
    penalty = 0
    for i in range(M):
        p, s = input().split()
        p = int(p) - 1
        if problems[p] == -1:
            continue
        if s == "WA":
            problems[p] += 1
        else:
            penalty += problems[p]
            problems[p] = -1
    print(problems.count(-1), penalty)
