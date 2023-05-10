def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s1, t1 = input().split()
        s.append(s1)
        t.append(int(t1))
    best = 0
    for i in range(n):
        if t[i] > t[best]:
            best = i
    print(best + 1)

if __name__ == '__main__':
    main()