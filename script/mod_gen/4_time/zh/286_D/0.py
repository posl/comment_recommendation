def main():
    n,x = map(int, input().split())
    total = 0
    for i in range(n):
        a,b = map(int, input().split())
        total += a * b
        if total > x * 100:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()