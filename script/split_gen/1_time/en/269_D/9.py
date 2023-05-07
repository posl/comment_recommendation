def main():
    # Get input
    n = int(input())
    coords = []
    for i in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))
    # Get all the hexagons
    hexagons = set()
    for x, y in coords:
        hexagons.add((x, y))
        hexagons.add((x + 1, y))
        hexagons.add((x - 1, y))
        hexagons.add((x, y + 1))
        hexagons.add((x, y - 1))
        hexagons.add((x + 1, y - 1))
        hexagons.add((x - 1, y + 1))
    # Get all the connected components
    components = []
    while hexagons:
        component = set()
        # Get the first hexagon
        hexagon = hexagons.pop()
        component.add(hexagon)
        # Get all the connected hexagons
        while component:
            new_hexagon = component.pop()
            for x, y in [(new_hexagon[0] + 1, new_hexagon[1]),
                         (new_hexagon[0] - 1, new_hexagon[1]),
                         (new_hexagon[0], new_hexagon[1] + 1),
                         (new_hexagon[0], new_hexagon[1] - 1),
                         (new_hexagon[0] + 1, new_hexagon[1] - 1),
                         (new_hexagon[0] - 1, new_hexagon[1] + 1)]:
                if x in range(-1001, 1002) and y in range(-1001, 1002):
                    if x % 2 == 0 and y % 2 == 0:
                        if (x, y) in hexagons:
                            component.add((x, y))
                            hexagons.remove((x, y))
        components.append(component)
    # Print the answer
    print(len(components))
