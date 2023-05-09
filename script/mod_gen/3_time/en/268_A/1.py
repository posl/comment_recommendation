def main():
    # read input
    a, b, c, d, e = map(int, input().split())
    # print output
    print(len(set([a, b, c, d, e])))

if __name__ == '__main__':
    main()