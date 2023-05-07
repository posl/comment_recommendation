def main():
    A,B,C,D = map(int,input().split())
    if A <= B * D:
        print(-1)
    else:
        count = 0
        while True:
            if (A - C * count) <= B * count:
                print(count)
                break
            count += 1

if __name__ == '__main__':
    main()