def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if (s - a) & 1 == 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()