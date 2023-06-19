def main():
    num = int(input())
    last = 0
    count = 0
    for i in range(num):
        a, b = map(int, input().split())
        if a == b:
            count += 1
            if count == 3:
                print("Yes")
                return
        else:
            count = 0
        last = a
    print("No")

if __name__ == '__main__':
    main()