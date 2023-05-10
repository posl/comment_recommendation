def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        tmp = input().split()
        s.append(tmp[0])
        t.append(tmp[1])
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()