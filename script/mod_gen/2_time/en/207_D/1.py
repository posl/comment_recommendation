def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int,input().split())))
    for i in range(n):
        t.append(list(map(int,input().split())))
    s.sort()
    t.sort()
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                continue
            else:
                dx = t[j][0] - s[i][0]
                dy = t[j][1] - s[i][1]
                for k in range(n):
                    if s[k][0] + dx == t[k][0] and s[k][1] + dy == t[k][1]:
                        continue
                    else:
                        break
                else:
                    print("Yes")
                    exit()
    print("No")
main()

if __name__ == '__main__':
    main()