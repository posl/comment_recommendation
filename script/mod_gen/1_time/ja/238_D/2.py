def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        elif (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()