def main():
    #a = int(input())
    #b = int(input())
    #c = int(input())
    #s = input()
    x1, y1, x2, y2 = map(int, input().split())
    #l = list(map(int, input().split()))
    #n = int(input())
    #s = input()
    #s = list(input())
    #s, t = input().split()
    #n = int(input())
    #a = list(map(int, input().split()))
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, input().split())) for _ in range(n)]
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 == ((x1 - 0) ** 2 + (y1 - 0) ** 2) ** 0.5 + ((x2 - 0) ** 2 + (y2 - 0) ** 2) ** 0.5:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()