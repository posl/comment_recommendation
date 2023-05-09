def main():
    # Read input
    S = []
    for i in range(9):
        S.append(input())
    # Count squares
    count = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == "#":
                if r > 0 and c > 0 and S[r - 1][c - 1] == "#":
                    if r > 0 and c < 8 and S[r - 1][c + 1] == "#":
                        if r < 8 and c < 8 and S[r + 1][c + 1] == "#":
                            if r < 8 and c > 0 and S[r + 1][c - 1] == "#":
                                count += 1
    # Print output
    print(count)
