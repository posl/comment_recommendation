def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    max_road = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                max_road += 1
    print(max_road - 2)
