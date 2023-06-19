def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k*d <= x:
        print(x-k*d)
    else:
        t = x//d
        if (k-t)%2 == 0:
            print(x-t*d)
        else:
            print(d-(x-t*d))

if __name__ == '__main__':
    main()