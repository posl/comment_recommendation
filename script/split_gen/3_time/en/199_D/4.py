def main():
    n, m = map(int, input().split())
    if m == 0:
        print(pow(3, n))
        return
    edge = [list(map(int, input().split())) for _ in range(m)]
    edge.sort()
    if edge[0][0] == 1:
        print(0)
        return
    for i in range(m - 1):
        if edge[i][0] == edge[i + 1][0] and edge[i][1] == edge[i + 1][1]:
            print(0)
            return
    print(pow(3, n - m))
main()
