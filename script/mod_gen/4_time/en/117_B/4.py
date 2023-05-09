def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    print("Yes" if l[-1] < sum(l[:-1]) else "No")

if __name__ == '__main__':
    main()