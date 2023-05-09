def problems274_b():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    for i in range(W):
        count = 0
        for j in range(H):
            if C[j][i] == '#':
                count += 1
        print(count)

if __name__ == '__main__':
    problems274_b()