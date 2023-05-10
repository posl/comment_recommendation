def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(sum(a[:-1]))
    print(sum(a[:-1]) + a[-1] - 1)

if __name__ == '__main__':
    main()