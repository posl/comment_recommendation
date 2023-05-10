def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = list(map(int, input().split()))
        l.pop(0)
        s.add(tuple(l))
    print(len(s))

if __name__ == '__main__':
    main()