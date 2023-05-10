def main():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[1])
    max_floor = ladders[0][1]
    for ladder in ladders[1:]:
        if ladder[0] < max_floor:
            max_floor = ladder[0]
    print(max_floor - 1)

if __name__ == '__main__':
    main()