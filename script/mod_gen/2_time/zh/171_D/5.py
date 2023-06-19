def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for _ in range(q):
        bc.append(list(map(int, input().split())))
    s = sum(a)
    for b, c in bc:
        s += (c - b) * a.count(b)
        print(s)
        a = list(map(lambda x: c if x == b else x, a))

if __name__ == '__main__':
    main()