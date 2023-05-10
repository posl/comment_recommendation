def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s1, t1 = input().split()
        s.append(s1)
        t.append(t1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] and t[i] == t[j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()