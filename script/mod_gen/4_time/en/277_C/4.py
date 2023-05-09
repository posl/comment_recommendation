def main():
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[1])
    current = 1
    for ladder in ladders:
        if current < ladder[0]:
            current = ladder[0]
        current = ladder[1]
    print(current)

if __name__ == '__main__':
    main()