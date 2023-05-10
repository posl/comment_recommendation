def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] < 0 and a[-1] < 0:
        a = [-i for i in a]
    if a[0] < 0 and a[-1] > 0:
        a = [-i for i in a]
        print(sum(a) + 2 * a[0])
    if a[0] > 0 and a[-1] > 0:
        print(sum(a) - 2 * a[0])

if __name__ == '__main__':
    main()