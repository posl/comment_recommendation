def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    Q = int(input())
    d = deque()
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                d.append(query[1])
        elif query[0] == 2:
            print(sum([d.popleft() for j in range(query[1])]))

if __name__ == '__main__':
    main()