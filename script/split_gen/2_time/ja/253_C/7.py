def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict, deque
    Q = int(input())
    a = defaultdict(int)
    b = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]] += 1
            b.append(query[1])
        elif query[0] == 2:
            if a[query[1]] > 0:
                a[query[1]] -= 1
                b.append(query[1])
        else:
            while b:
                q = b.popleft()
                if a[q] > 0:
                    a[q] -= 1
                    print(q - b[0])
                    break
