def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0] + x[1], reverse=True)
    aoki = sum([a for a, b in ab])
    takahashi = 0
    for i in range(n):
        takahashi += ab[i][0]
        aoki -= ab[i][0]
        if takahashi > aoki:
            print(i + 1)
            break

if __name__ == '__main__':
    main()