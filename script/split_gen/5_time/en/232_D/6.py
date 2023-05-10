def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    print(sum([1 for i in range(h) for j in range(w) if c[i][j] == '.']))
