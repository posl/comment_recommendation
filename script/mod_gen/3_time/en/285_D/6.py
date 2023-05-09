def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        if s[i] in t:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()