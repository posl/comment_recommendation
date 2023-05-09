def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if a == s:
            print("Yes")
            continue
        d = s - a
        if d % 2 == 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()