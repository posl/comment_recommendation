def main():
    n, m = map(int, input().split())
    problems = [None] * n
    for i in range(n):
        problems[i] = [0, 0]
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if problems[p][0] == 0:
            if s == 'AC':
                problems[p][0] = 1
            else:
                problems[p][1] += 1
    correct = 0
    penalty = 0
    for i in range(n):
        if problems[i][0] == 1:
            correct += 1
            penalty += problems[i][1]
    print(correct, penalty)
