def main():
    r, c = map(int, input().split())
    a = []
    for _ in range(2):
        a.append(list(map(int, input().split())))
    print(a[r-1][c-1])
