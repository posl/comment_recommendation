def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    AB = [0] + AB
    for i in range(1, M + 1):
        if AB[i][0] + 1 == AB[i][1] or AB[i][0] - 1 == AB[i][1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()