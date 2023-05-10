def main():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    #s = input().split()
    #s = [input() for _ in range(n)]
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(101):
        for j in range(101):
            x, y, h = a[0]
            H = h + abs(x-i) + abs(y-j)
            if all(h == max(H - abs(x-i) - abs(y-j), 0) for x, y, h in a):
                print(i, j, H)
                exit()

if __name__ == '__main__':
    main()