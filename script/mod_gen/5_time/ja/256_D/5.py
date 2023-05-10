def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    print(l[0], r[n-1]+1)

if __name__ == '__main__':
    main()