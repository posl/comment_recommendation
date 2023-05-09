def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 1:
            if k % 3 == 1:
                print(s[0])
            elif k % 3 == 2:
                print(s[1])
            else:
                print(s[2])
        elif t % 3 == 2:
            if k % 3 == 1:
                print(s[1])
            elif k % 3 == 2:
                print(s[2])
            else:
                print(s[0])
        else:
            if k % 3 == 1:
                print(s[2])
            elif k % 3 == 2:
                print(s[0])
            else:
                print(s[1])

if __name__ == '__main__':
    main()