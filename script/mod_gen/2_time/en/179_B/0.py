def main():
    n = int(input())
    for i in range(n - 2):
        d1, d2 = map(int, input().split())
        d3, d4 = map(int, input().split())
        d5, d6 = map(int, input().split())
        if d1 == d2 and d3 == d4 and d5 == d6:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()