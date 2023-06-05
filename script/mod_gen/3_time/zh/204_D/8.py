def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    if n == 2:
        print(t[1])
    else:
        t1 = t[n - 1]
        t2 = t[n - 2]
        for i in range(n - 3, -1, -1):
            if t1 <= t2:
                t1 += t[i]
            else:
                t2 += t[i]
        print(max(t1, t2))

if __name__ == '__main__':
    main()