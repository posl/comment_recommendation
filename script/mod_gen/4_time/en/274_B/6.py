def main():
    h, w = map(int, input().split())
    grid = [input() for i in range(h)]
    for i in range(w):
        print(sum([1 if grid[j][i] == '#' else 0 for j in range(h)]))

if __name__ == '__main__':
    main()