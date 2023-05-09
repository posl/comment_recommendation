def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k*d:
        print(x - k*d)
    else:
        if (k*d - x) % (2*d) == 0:
            print(0)
        else:
            print(abs((k*d - x) % (2*d) - d))

if __name__ == '__main__':
    main()