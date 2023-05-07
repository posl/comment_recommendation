def main():
    N, W = map(int, input().split())
    event = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        event.append((S, P))
        event.append((T, -P))
    event.sort(key=lambda x: x[0])
    now = 0
    for _, P in event:
        now += P
        if now > W:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()