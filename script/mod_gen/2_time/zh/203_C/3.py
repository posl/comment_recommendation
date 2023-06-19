def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    money = k
    for i in range(n):
        if money < ab[i][0]:
            print(money)
            return
        money += ab[i][1]
    print(money)

if __name__ == '__main__':
    main()