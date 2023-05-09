def solve():
    N = int(input())
    task = []
    for _ in range(N):
        a, b = map(int, input().split())
        task.append((a, b))
    task.sort(key=lambda x: x[1])
    time = 0
    for a, b in task:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")
solve()
