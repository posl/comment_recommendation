def main():
    n = int(input())
    lst = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        lst.append([t, s])
    lst.sort(reverse=True)
    print(lst[1][1])

if __name__ == '__main__':
    main()