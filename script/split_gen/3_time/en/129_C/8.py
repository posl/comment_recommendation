def count_ways(N, M, broken_steps):
    if N == 1:
        return 1
    if N == 2:
        return 2 if 1 not in broken_steps else 1
    if N == 3:
        return 4 if 1 not in broken_steps and 2 not in broken_steps else 2 if 1 in broken_steps or 2 in broken_steps else 3
    count = [0 for _ in range(N + 1)]
    count[0] = 1
    count[1] = 1 if 1 not in broken_steps else 0
    count[2] = 2 if 1 not in broken_steps else 1
    for i in range(3, N + 1):
        if i not in broken_steps:
            count[i] = count[i - 1] + count[i - 2]
            count[i] %= 1000000007
    return count[N]
N, M = map(int, input().split())
broken_steps = set()
for _ in range(M):
    broken_steps.add(int(input()))
print(count_ways(N, M, broken_steps))
