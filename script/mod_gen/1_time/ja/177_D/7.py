def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[0])
    ans = 1
    for i in range(M - 1):
        if AB[i][0] != AB[i + 1][0]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()