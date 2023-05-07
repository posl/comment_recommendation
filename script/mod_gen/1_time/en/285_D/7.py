def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(N):
        for j in range(N):
            if i != j and s[i] == s[j]:
                print("No")
                exit(0)
            if i != j and t[i] == t[j]:
                print("No")
                exit(0)
    print("Yes")

if __name__ == '__main__':
    main()