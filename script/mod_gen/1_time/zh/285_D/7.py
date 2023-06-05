def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        temp = input().split()
        s.append(temp[0])
        t.append(temp[1])
    for i in range(n):
        if s[i] in t:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()