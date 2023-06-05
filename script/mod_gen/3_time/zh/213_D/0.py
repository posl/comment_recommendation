def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    ab.sort(key=lambda x: (x[0], x[1]))
    print(ab)
    for i in ab:
        print(i[0], i[1])

if __name__ == '__main__':
    main()