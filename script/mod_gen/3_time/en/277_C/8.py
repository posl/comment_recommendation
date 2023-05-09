def main():
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[0])
    last_floor = ladders[0][0]
    for ladder in ladders:
        if ladder[0] != last_floor:
            print(last_floor)
            exit()
        last_floor = ladder[1]
    print(last_floor)

if __name__ == '__main__':
    main()