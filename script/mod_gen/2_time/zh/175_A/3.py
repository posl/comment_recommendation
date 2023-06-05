def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = n - r
    if r == 0 or w == 0:
        print(0)
    else:
        print(c[:r].count('W'))

if __name__ == '__main__':
    main()