def main():
    n = int(input())
    xy = []
    for i in range(n):
        xy.append(list(map(int, input().split())))
    print(xy)

if __name__ == '__main__':
    main()