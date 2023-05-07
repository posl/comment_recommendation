def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    sumA = 0
    sumB = 0
    for i in range(N):
        sumA += AB[i][0] / AB[i][1]
        sumB += 1 / AB[i][1]
    print(sumA / sumB)

if __name__ == '__main__':
    main()