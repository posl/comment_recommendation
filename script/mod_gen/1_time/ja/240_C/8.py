def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1])
    for a, b in AB:
        if X < a:
            print("No")
            return
        X -= a
    if X == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()