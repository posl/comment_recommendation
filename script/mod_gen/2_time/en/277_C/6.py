def main():
    N = int(input())
    ladders = [tuple(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[0])
    pos = 1
    for a, b in ladders:
        if a <= pos <= b:
            pos = b if a == pos else a
    print(pos)

if __name__ == '__main__':
    main()