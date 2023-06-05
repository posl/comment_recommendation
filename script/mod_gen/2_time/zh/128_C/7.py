def main():
    n = int(input())
    lst = []
    for i in range(n):
        s, p = input().split()
        lst.append((s, int(p), i + 1))
    lst.sort(key=lambda x: (x[0], -x[1]))
    for item in lst:
        print(item[2])

if __name__ == '__main__':
    main()