def main():
    n = int(input())
    flag = False
    for i in range(n-2):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            d3, d4 = map(int, input().split())
            if d3 == d4:
                d5, d6 = map(int, input().split())
                if d5 == d6:
                    flag = True
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()