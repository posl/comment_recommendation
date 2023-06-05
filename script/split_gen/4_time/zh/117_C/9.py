def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(abs(x[0]))
    else:
        x2 = list(map(lambda x: x * -1, x))
        x2.sort()
        print(min(abs(x[0]), abs(x2[0]), abs(x[0]) * 2 + abs(x2[0]), abs(x2[0]) * 2 + abs(x[0])))
