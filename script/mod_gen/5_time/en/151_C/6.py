def solve():
    N, M = map(int, input().split())
    problems = [0] * N
    penalties = [0] * N
    for _ in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            problems[p-1] = 1
        else:
            if problems[p-1] == 0:
                penalties[p-1] += 1
    print(sum(problems), sum([p * problems[i] for i, p in enumerate(penalties)]))

if __name__ == '__main__':
    solve()