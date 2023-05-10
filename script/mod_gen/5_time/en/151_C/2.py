def main():
    n, m = map(int, input().split())
    problems = [0] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p)
        if problems[p-1] == 0 and s == 'WA':
            wa[p-1] += 1
        elif problems[p-1] == 0 and s == 'AC':
            problems[p-1] = 1
    print('{} {}'.format(sum(problems), sum([i*j for i,j in zip(problems, wa)])))

if __name__ == '__main__':
    main()