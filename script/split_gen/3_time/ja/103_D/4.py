def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab = sorted(ab, key=lambda x: x[1])
    count = 1
    bridge = ab[0][1]
    for i in range(1, m):
        if bridge <= ab[i][0]:
            count += 1
            bridge = ab[i][1]
    print(m - count)
main()
