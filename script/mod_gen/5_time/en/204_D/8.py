def main():
    n = int(input())
    t = [int(x) for x in input().split()]
    t.sort()
    print(t[-1])

if __name__ == '__main__':
    main()