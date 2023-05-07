def main():
    n = int(input())
    data = [input().split() for _ in range(n)]
    data = sorted(data, key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(data[i][2])

if __name__ == '__main__':
    main()