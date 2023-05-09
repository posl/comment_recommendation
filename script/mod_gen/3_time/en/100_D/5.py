def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                cakes.sort(key=lambda x: (-1)**a * x[0] + (-1)**b * x[1] + (-1)**c * x[2], reverse=True)
                ans = max(ans, sum((-1)**a * x[0] + (-1)**b * x[1] + (-1)**c * x[2] for x in cakes[:M]))
    print(ans)

if __name__ == '__main__':
    main()