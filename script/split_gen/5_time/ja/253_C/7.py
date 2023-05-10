def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    from heapq import heapify, heappop, heappush
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    S = []
    S_cnt = Counter()
    S_min = 10**9+1
    S_max = -1
    for q in query:
        if q[0] == "1":
            x = int(q[1])
            S.append(x)
            S_cnt[x] += 1
            S_min = min(S_min, x)
            S_max = max(S_max, x)
        elif q[0] == "2":
            x = int(q[1])
            c = int(q[2])
            while c > 0:
                if S_cnt[x] > 0:
                    S_cnt[x] -= 1
                    S.remove(x)
                    c -= 1
                else:
                    break
            if S_cnt[x] == 0:
                S_min = min(S)
                S_max = max(S)
        else:
            print(S_max - S_min)
main()
