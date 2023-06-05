def main():
    n, w = map(int, input().split())
    events = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    for _, p in events:
        w -= p
        if w < 0:
            print("No")
            return
    print("Yes")
