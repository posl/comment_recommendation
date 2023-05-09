def main():
    lines = []
    for i in range(9):
        lines.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if lines[i][j] == "#":
                count += 1
    print(count)
