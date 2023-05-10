def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(zip(range(1, n+1), a, b))
    c = sorted(c, key=lambda x: -x[1])
    c = sorted(c[:x+y+z], key=lambda x: -x[2]-x[1])
    for i in range(x+y+z):
        print(c[i][0])

if __name__ == '__main__':
    main()