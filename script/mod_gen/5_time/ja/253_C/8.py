def main():
    from collections import Counter
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.buffer.readline
    q = int(input())
    add = []
    dels = []
    c = Counter()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            add.append(query[1])
        elif query[0] == 2:
            dels.append(query[1])
            c[query[1]] += 1
        else:
            while add:
                if c[add[-1]] > 0:
                    c[add[-1]] -= 1
                    add.pop()
                else:
                    break
            while dels:
                if c[dels[-1]] == 0:
                    dels.pop()
                else:
                    break
            print(add[-1] - dels[-1])

if __name__ == '__main__':
    main()