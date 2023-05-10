def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(x) for x in a])
    print(sum([sum(x) for x in a]) - min_a * h * w)
