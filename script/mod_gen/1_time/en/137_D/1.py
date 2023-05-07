def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    reward = 0
    day = 1
    for A, B in jobs:
        if A <= day:
            continue
        if A - day > M:
            break
        M -= A - day
        day = A
        reward += B
    print(reward)

if __name__ == '__main__':
    main()