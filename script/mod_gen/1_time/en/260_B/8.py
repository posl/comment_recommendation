def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = [(i, a[i], b[i]) for i in range(n)]
    ab.sort(key=lambda x: x[1], reverse=True)
    ab.sort(key=lambda x: x[2], reverse=True)
    ab.sort(key=lambda x: x[1]+x[2], reverse=True)
    for i in range(x+y+z):
        print(ab[i][0]+1)

if __name__ == '__main__':
    main()