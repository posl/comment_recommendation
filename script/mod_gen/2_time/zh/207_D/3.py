def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append([int(j) for j in input().split()])
    for i in range(n):
        t.append([int(j) for j in input().split()])
    s.sort()
    t.sort()
    for i in range(n):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()