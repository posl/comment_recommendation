def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    s.sort()
    t.sort()
    for i in range(4):
        if s == t:
            print("Yes")
            exit()
        s = rotate(s, 90)
    print("No")

if __name__ == '__main__':
    main()