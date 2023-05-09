def main():
    n, d = map(int, input().split())
    walls = []
    for i in range(n):
        l, r = map(int, input().split())
        walls.append((l, r))
    walls = sorted(walls)
    count = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and walls[j][0] <= walls[i][1] + d:
            j += 1
        count += 1
        i = j
    print(count)

if __name__ == '__main__':
    main()