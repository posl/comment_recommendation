def main():
    N = int(input())
    black_cells = []
    for i in range(N):
        x,y = map(int,input().split())
        black_cells.append((x,y))
    black_cells.sort()
    black_cells = list(set(black_cells))
    print(black_cells)
    return

if __name__ == '__main__':
    main()