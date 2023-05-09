def main():
    n = int(input())
    l = [int(i) for i in input().split()]
    lmax = max(l)
    if lmax < sum(l) - lmax:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()