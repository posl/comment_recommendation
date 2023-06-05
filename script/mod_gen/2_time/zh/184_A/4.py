def main():
    N, W = map(int, input().split())
    person = []
    for i in range(N):
        person.append(list(map(int, input().split())))
    person.sort()
    water = 0
    for i in range(N):
        water += person[i][2]
        if water > W:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()