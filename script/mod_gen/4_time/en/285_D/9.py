def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        x,y = input().split()
        s.append(x)
        t.append(y)
    for i in range(n):
        if s[i] == t[i]:
            print("No")
            return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == t[j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()