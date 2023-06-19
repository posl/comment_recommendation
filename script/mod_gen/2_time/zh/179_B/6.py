def main():
    n = int(input())
    flag = False
    count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
        else:
            count = 0
        if count >= 3:
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()