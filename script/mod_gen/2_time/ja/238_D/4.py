def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a == 0 and s == 0:
            print("Yes")
        elif a == 0 or s == 0:
            print("No")
        elif a > s:
            print("No")
        else:
            if (s - a) % 2 == 0:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()