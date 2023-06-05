def main():
    a,b = map(int, input().split())
    c = b/a
    print("{0:.3f}".format(c))

if __name__ == '__main__':
    main()