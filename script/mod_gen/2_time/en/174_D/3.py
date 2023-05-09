def main():
    n = int(input())
    c = input()
    r = c.count("R")
    w = c.count("W")
    if r == 0 or w == 0:
        print(0)
        return
    r = c[:r].count("W")
    print(r)

if __name__ == '__main__':
    main()