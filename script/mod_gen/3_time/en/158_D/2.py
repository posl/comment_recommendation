def main():
    s = input()
    q = int(input())
    reverse = False
    for _ in range(q):
        t = input().split()
        if t[0] == '1':
            reverse = not reverse
        else:
            if t[1] == '1':
                if reverse:
                    s = s + t[2]
                else:
                    s = t[2] + s
            else:
                if reverse:
                    s = t[2] + s
                else:
                    s = s + t[2]
    if reverse:
        s = s[::-1]
    print(s)

if __name__ == '__main__':
    main()