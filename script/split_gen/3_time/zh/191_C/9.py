def main():
    h,w = list(map(int, input().strip().split()))
    s = []
    for i in range(h):
        s.append(input().strip())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)
