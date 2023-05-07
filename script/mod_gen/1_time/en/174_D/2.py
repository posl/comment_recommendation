def main():
    N = int(input())
    c = input()
    R = c.count('R')
    W = c.count('W')
    if R == 0 or W == 0:
        print(0)
        return
    print(min(c[:R].count('W'), c[-W:].count('R')))
main()

if __name__ == '__main__':
    main()