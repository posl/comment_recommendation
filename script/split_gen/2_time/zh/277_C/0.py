def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    last = 0
    for i in range(n):
        if ab[i][0] > last:
            last = ab[i][1] - 1
    print(last)
