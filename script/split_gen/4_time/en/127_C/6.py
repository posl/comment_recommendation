def main():
    n, m = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    l = [i[0] for i in lr]
    r = [i[1] for i in lr]
    print(max(0, min(r) - max(l) + 1))
