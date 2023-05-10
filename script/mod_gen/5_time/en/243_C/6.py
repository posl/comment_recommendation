def main():
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    print(solve(N, XY, S))

if __name__ == '__main__':
    main()