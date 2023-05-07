def main():
    from bisect import bisect_left
    from collections import Counter
    Q = int(input())
    S = Counter()
    S_list = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S[query[1]] += 1
            S_list.append(query[1])
            S_list.sort()
        elif query[0] == 2:
            if S[query[1]] >= query[2]:
                S[query[1]] -= query[2]
                for _ in range(query[2]):
                    S_list.pop(bisect_left(S_list, query[1]))
            else:
                S[query[1]] = 0
                for _ in range(S[query[1]]):
                    S_list.pop(bisect_left(S_list, query[1]))
        else:
            print(S_list[-1] - S_list[0])
