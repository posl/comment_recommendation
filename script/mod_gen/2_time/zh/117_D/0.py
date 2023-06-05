def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    dis = []
    for i in range(m - 1):
        dis.append(x[i + 1] - x[i])
    dis.sort()
    print(sum(dis[:m - n]))

if __name__ == '__main__':
    main()