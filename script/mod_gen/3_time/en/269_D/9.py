def main():
    N = int(input())
    cells = []
    for i in range(N):
        cells.append([int(x) for x in input().split(' ')])
    cells.sort()
    cells = [cells[0]] + [cells[i] for i in range(1, N) if cells[i] != cells[i-1]]
    print(len(cells))

if __name__ == '__main__':
    main()