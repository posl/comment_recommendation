def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    distance = []
    for i in range(1, m):
        distance.append(x[i] - x[i - 1])
    distance.sort()
    print(sum(distance[:m - n]))

if __name__ == '__main__':
    main()