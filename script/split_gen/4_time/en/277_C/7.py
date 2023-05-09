def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1], reverse=True)
    floor = ab[0][1]
    for i in range(1, n):
        if floor <= ab[i][0]:
            floor = ab[i][0] - 1
        else:
            floor = ab[i][1]
    print(floor)
