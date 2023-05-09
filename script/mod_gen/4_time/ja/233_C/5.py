def main():
    n, x = map(int, input().split())
    bags = []
    for i in range(n):
        bags.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(bags[i][0]):
            count += bags[i][j+1]
    if count < x:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()