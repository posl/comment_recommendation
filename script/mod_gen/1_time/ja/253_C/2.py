def main():
    from collections import defaultdict
    from bisect import bisect_left, bisect_right
    Q = int(input())
    S = []
    d = defaultdict(int)
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            S.append(q[1])
            d[q[1]] += 1
        elif q[0] == 2:
            if d[q[1]] > 0:
                d[q[1]] -= 1
                S.remove(q[1])
        else:
            print(max(S) - min(S))

if __name__ == '__main__':
    main()