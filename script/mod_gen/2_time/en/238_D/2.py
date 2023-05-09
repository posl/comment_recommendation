def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a == 0 and s == 0:
            print("Yes")
        elif a == 0:
            print("No")
        elif a > s:
            print("No")
        elif (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()