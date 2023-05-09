def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().split()[0])
        t.append(input().split()[0])
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()