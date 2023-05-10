def main():
    x, y = map(int, raw_input().split())
    print "Yes" if x + 3 > y else "No"

if __name__ == '__main__':
    main()