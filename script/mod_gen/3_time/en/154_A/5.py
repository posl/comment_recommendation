def main():
    # get input
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    # process
    if s == u:
        a -= 1
    else:
        b -= 1
    # output
    print(a, b)

if __name__ == '__main__':
    main()