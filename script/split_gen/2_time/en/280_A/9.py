def main():
    #Read input data
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    #Count the number of squares with pieces
    count = 0
    for i in range(H):
        count += S[i].count("#")
    #Print the number of squares with pieces
    print(count)
