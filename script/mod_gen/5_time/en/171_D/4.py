def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for i in range(q):
        bc.append(list(map(int, input().split())))
    a.sort()
    s = sum(a)
    for i in range(q):
        s += (bc[i][1] - bc[i][0]) * a.count(bc[i][0])
        print(s)
        a = list(map(lambda x: bc[i][1] if x == bc[i][0] else x, a))

if __name__ == '__main__':
    main()