def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    #print(t)
    t1 = 0
    t2 = 0
    for i in range(n):
        if t1 < t2:
            t1 += t[-1-i]
        else:
            t2 += t[-1-i]
    print(max(t1, t2))

if __name__ == '__main__':
    main()