def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] and t[i] == t[j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()