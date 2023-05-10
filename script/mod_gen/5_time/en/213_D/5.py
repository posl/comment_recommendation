def main():
    N = int(input())
    AB = []
    for i in range(N-1):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    print(1, end=' ')
    for i in range(N-1):
        print(AB[i][1], end=' ')
    print(1)

if __name__ == '__main__':
    main()