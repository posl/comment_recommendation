def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    a_max = a[-1]
    for i in range(n):
        if a_max == a[i]:
            print(a[-2])
        else:
            print(a_max)

if __name__ == '__main__':
    main()