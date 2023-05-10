def main():
    cost = 0
    a = list(map(int, input().split()))
    a.sort()
    cost = a[2] - a[0]
    print(cost)

if __name__ == '__main__':
    main()