def main():
    # input
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    # compute
    from collections import defaultdict
    d = defaultdict(int)
    min_val = 10**9
    max_val = 0
    for q in query:
        if q[0] == '1':
            x = int(q[1])
            d[x] += 1
            if x < min_val:
                min_val = x
            if x > max_val:
                max_val = x
        elif q[0] == '2':
            x = int(q[1])
            c = int(q[2])
            if d[x] > 0:
                if d[x] <= c:
                    d[x] = 0
                else:
                    d[x] -= c
        else:
            print(max_val-min_val)
