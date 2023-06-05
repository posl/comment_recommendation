def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    t1 = 0
    t2 = 0
    for i in range(n):
        if t1 <= t2:
            t1 += t[i]
        else:
            t2 += t[i]
    print(max(t1, t2))

if __name__ == '__main__':
    main()