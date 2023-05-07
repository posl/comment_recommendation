def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[0] + sum(t[1:]) - t[0] // 2)

if __name__ == '__main__':
    main()