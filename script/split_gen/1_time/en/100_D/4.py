def main():
    n, m = map(int, input().split())
    cakes = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        cakes.append(x + y + z)
        cakes.append(x + y - z)
        cakes.append(x - y + z)
        cakes.append(x - y - z)
    cakes.sort(reverse=True)
    print(sum(cakes[:m]))
main()
