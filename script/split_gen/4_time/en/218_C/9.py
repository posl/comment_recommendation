def get_shapes(grid):
    shapes = []
    for row in grid:
        for col in row:
            if col == "#":
                shapes.append((row.index(col), grid.index(row)))
                break
    return shapes
