def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))
    ans = 0
    for i in range(2**3):
        cakes.sort(key=lambda x: (-1)**(i & 1) * x[(i & 2) >> 1] + (-1)**(i & 4) * x[(i & 8) >> 3] + (-1)**(i & 16) * x[(i & 32) >> 5], reverse=True)
        ans = max(ans, sum(cakes[j][0] + cakes[j][1] + cakes[j][2] for j in range(M)))
    print(ans)
main()

if __name__ == '__main__':
    main()