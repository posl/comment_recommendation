def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    print(sum([min(a[i]) for i in range(h)]) * w - sum([sum(a[i]) for i in range(h)]))
