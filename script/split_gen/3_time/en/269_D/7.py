def check_black_neighbours(x, y):
    if (x-1,y-1) in black_cells:
        return True
    if (x-1,y) in black_cells:
        return True
    if (x,y-1) in black_cells:
        return True
    if (x,y+1) in black_cells:
        return True
    if (x+1,y) in black_cells:
        return True
    if (x+1,y+1) in black_cells:
        return True
    return False
black_cells = []
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    black_cells.append((x,y))
