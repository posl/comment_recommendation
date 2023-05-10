def main():
    H, W = map(int, input().split())
    c = []
    for i in range(H):
        c.append(input())
    for i in range(W):
        count = 0
        for j in range(H):
            if c[j][i] == '#':
                count += 1
        print(count)
