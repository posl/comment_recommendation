def main():
    #S = [input() for i in range(9)]
    S = [".#.......","#.#......",".#.......",".........","....#.#.#",".........","....#.#.#",".........","........."]
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                count += 1
    print(count)