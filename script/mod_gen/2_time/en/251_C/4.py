def main():
    N = int(input())
    submissions = []
    for i in range(N):
        S, T = input().split()
        submissions.append([S, int(T), i + 1])
    submissions = sorted(submissions, key=lambda x: x[2])
    submissions = sorted(submissions, key=lambda x: x[1], reverse=True)
    best = []
    for i in range(N):
        if submissions[i][0] not in [s[0] for s in best]:
            best.append(submissions[i])
    print(best[0][2])

if __name__ == '__main__':
    main()