def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = input().split()
        l = l[1:]
        s.add(tuple(l))
    print(len(s))

if __name__ == '__main__':
    main()