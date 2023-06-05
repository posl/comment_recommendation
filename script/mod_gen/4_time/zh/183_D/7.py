def main():
    n, w = map(int, input().split())
    events = []
    for i in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    current = 0
    for _, p in events:
        current += p
        if current > w:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()