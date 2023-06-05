def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    s = sum(a)
    for i in range(q):
        b, c = map(int, input().split())
        s += (c - b) * a.count(b)
        print(s)
        a = [c if x == b else x for x in a]

if __name__ == '__main__':
    main()