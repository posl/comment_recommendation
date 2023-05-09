def main():
    n = int(input())
    data = [input().split() for _ in range(n)]
    data = [(data[i][0], int(data[i][1]), i+1) for i in range(n)]
    data.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(data[i][2])

if __name__ == '__main__':
    main()