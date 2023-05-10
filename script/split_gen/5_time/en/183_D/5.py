def main():
    N, W = map(int, input().split())
    plan = [tuple(map(int, input().split())) for _ in range(N)]
    event = []
    for s, t, p in plan:
        event.append((s, p))
        event.append((t, -p))
    event.sort()
    current = 0
    for _, p in event:
        current += p
        if current > W:
            print("No")
            exit()
    print("Yes")
