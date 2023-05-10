def main():
    from sys import stdin
    from collections import Counter
    readline = stdin.readline
    q = int(readline())
    A = []
    for _ in range(q):
        query = list(map(int,readline().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if len(A) > 0:
                cnt = Counter(A)
                for i in range(min(query[2],cnt[query[1]])):
                    A.remove(query[1])
        else:
            A.sort()
            print(A[-1] - A[0])

if __name__ == '__main__':
    main()