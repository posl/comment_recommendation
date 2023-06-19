def main():
    h,w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(row) for row in a])
    print(sum([sum([x - min_a for x in row]) for row in a]))
