def main():
    N = int(input())
    c = input()
    print(c.count('W') + 1 - c.count('W', 0, c.find('R') + 1))

if __name__ == '__main__':
    main()