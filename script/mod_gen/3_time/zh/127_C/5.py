def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    if l[m-1] > r[0]:
        print(0)
    else:
        print(r[0] - l[m-1] + 1)

if __name__ == '__main__':
    main()