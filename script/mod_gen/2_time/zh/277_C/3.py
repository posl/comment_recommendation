def main():
    n = int(input())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1] - x[0])
    #print(ab)
    now = 1
    for a, b in ab:
        if b <= now:
            continue
        else:
            now = b
    print(now)

if __name__ == '__main__':
    main()