def solve(N, trampolines):
    # 1. Make a list of distances from the 0-th trampoline
    distances = [abs(x) + abs(y) for x, y, p in trampolines]
    # 2. Make a list of powers of the 0-th trampoline
    powers = [p for x, y, p in trampolines]
    # 3. Make a list of the maximum distance that can be reached by each power
    max_dist = [0] * (max(powers) + 1)
    for i in range(N):
        max_dist[powers[i]] = max(max_dist[powers[i]], distances[i])
    # 4. Calculate the answer
    ans = 0
    for i in range(1, len(max_dist)):
        max_dist[i] = max(max_dist[i], max_dist[i - 1])
        ans += max_dist[i] // i + (1 if max_dist[i] % i else 0)
    return ans
N = int(input())
trampolines = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, trampolines))
This solution got 100 points.
I think this solution is not so efficient, but it is easy to understand.
This problem has been solved by some other people.
I think this problem is not so difficult, but it is a good exercise to practice dynamic programming.
I am looking forward to seeing your solutions.
I will post my solution to the next problem in a few days.
Thank you for reading.
I am a Japanese programmer. I am interested in programming contests and programming languages. I am interested in Haskell, Rust, and Python. I am also interested in functional programming and type theory. View all posts by yukicoder

if __name__ == '__main__':
    solve()