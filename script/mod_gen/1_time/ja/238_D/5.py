def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if a == s:
            print("Yes")
            continue
        if (s - a) % 2 == 0:
            print("Yes")
            continue
        print("No")

if __name__ == '__main__':
    main()