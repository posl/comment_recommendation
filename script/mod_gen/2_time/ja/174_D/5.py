def main():
    N = int(input())
    c = input()
    r = c.count("R")
    w = N - r
    print(min(r, w))

if __name__ == '__main__':
    main()