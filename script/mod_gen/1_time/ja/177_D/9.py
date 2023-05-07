def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[1])
    cnt = 0
    while AB:
        a, b = AB.pop(0)
        cnt += 1
        while AB:
            if AB[0][0] <= b:
                AB.pop(0)
            else:
                break
    print(cnt)

if __name__ == '__main__':
    main()