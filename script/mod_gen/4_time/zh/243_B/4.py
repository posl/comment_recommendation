def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = set(a) & set(b)
    print(len(s))
    d = {x: 0 for x in s}
    for x in a:
        d[x] += 1
    for x in b:
        d[x] += 1
    print(sum([1 for x in d if d[x] > 1]))

if __name__ == '__main__':
    main()