def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = input().split()
        s.add(tuple(l[1:]))
    print(len(s))

if __name__ == '__main__':
    main()