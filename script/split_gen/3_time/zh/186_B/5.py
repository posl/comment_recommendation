def main():
    h,w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(a[i]) for i in range(h)])
    print(sum([sum(a[i]) - min_a*w for i in range(h)]))
