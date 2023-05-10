def main():
    n = int(input())
    tka = []
    for i in range(n):
        tka.append(list(map(int, input().split())))
    tka.reverse()
    time = 0
    for i in range(n):
        if time % tka[i][0] != 0:
            time += tka[i][0] - (time % tka[i][0])
        time += tka[i][1]
    print(time)

if __name__ == '__main__':
    main()