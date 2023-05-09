def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a_max = max(a)
    a_max2 = max(a[:a.index(a_max)] + a[a.index(a_max)+1:])
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)

if __name__ == '__main__':
    main()