def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while M > 0 and i < N:
        a, b = jobs[i]
        if M < a:
            ans += M * b
            M = 0
        else:
            ans += a * b
            M -= a
        i += 1
    print(ans)

if __name__ == '__main__':
    main()