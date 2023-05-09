def main():
    s = input()
    q = int(input())
    t = []
    for i in range(q):
        t.append(input().split())
    for i in range(q):
        if t[i][0] == "1":
            s = s[::-1]
        else:
            if t[i][1] == "1":
                s = t[i][2] + s
            else:
                s = s + t[i][2]
    print(s)

if __name__ == '__main__':
    main()