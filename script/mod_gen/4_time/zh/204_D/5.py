def main():
    n = int(input())
    t = [int(i) for i in input().split()]
    t.sort()
    print(t[-1] + t[-2])

if __name__ == '__main__':
    main()