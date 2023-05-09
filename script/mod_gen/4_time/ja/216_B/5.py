def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        temp = input().split()
        s.append(temp[0])
        t.append(temp[1])
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j]:
                    if t[i] == t[j]:
                        print("Yes")
                        exit()
    print("No")

if __name__ == '__main__':
    main()