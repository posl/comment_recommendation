def main():
    from sys import stdin
    from collections import defaultdict
    from bisect import bisect_left
    read = stdin.buffer.read
    readline = stdin.buffer.readline
    readlines = stdin.buffer.readlines
    q = int(readline())
    s = defaultdict(int)
    a = []
    for _ in range(q):
        query = list(map(int,readline().split()))
        if query[0] == 1:
            s[query[1]] += 1
            a.append(query[1])
        elif query[0] == 2:
            for i in range(min(query[2],s[query[1]])):
                s[a.pop(bisect_left(a,query[1]))] -= 1
        else:
            print(a[-1] - a[0])

if __name__ == '__main__':
    main()