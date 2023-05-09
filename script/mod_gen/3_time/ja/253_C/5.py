def main():
    from collections import defaultdict
    from bisect import bisect_left, bisect_right
    from heapq import heappop, heappush, heapify
    from sys import stdin
    input = stdin.readline
    Q = int(input())
    S = []
    S_dict = defaultdict(int)
    S_dict[0] = 0
    S_dict[10**9] = 0
    S.append(0)
    S.append(10**9)
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S.append(query[1])
            S_dict[query[1]] += 1
        elif query[0] == 2:
            num = S_dict[query[1]]
            if num >= query[2]:
                S_dict[query[1]] -= query[2]
            else:
                S_dict[query[1]] = 0
            S_dict[0] += query[2] - num
        else:
            S.sort()
            print(S[-1] - S[0] - S_dict[0])

if __name__ == '__main__':
    main()