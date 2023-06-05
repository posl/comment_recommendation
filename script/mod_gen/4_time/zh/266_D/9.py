def main():
    n = int(input())
    txa = [list(map(int, input().split())) for i in range(n)]
    txa.insert(0, [0, 0, 0])
    result = 0
    for i in range(1, len(txa)):
        result += max(0, txa[i][2] - (txa[i][0] - txa[i - 1][0] - abs(txa[i][1] - txa[i - 1][1])))
    print(result)

if __name__ == '__main__':
    main()