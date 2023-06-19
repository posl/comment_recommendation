def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(n)]
    xy.sort(key=lambda x: x[0])
    print(xy)
