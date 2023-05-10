def main():
    # Take input here
    h, w = map(int, input().strip().split())
    s = [input().strip() for _ in range(h)]
    # Compute desired result here
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    # Print result here
    print(count)
