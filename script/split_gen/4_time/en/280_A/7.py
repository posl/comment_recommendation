def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum(row.count('#') for row in s))
