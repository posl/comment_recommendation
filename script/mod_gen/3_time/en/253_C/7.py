def main():
    from collections import Counter
    import heapq
    
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append([int(i) for i in input().split()])
    
    S = []
    heapq.heapify(S)
    counter = Counter()
    for query in queries:
        if query[0] == 1:
            heapq.heappush(S, query[1])
            counter[query[1]] += 1
        elif query[0] == 2:
            while query[2] > 0 and S:
                if counter[S[0]] <= query[2]:
                    query[2] -= counter[S[0]]
                    counter[S[0]] = 0
                    heapq.heappop(S)
                else:
                    counter[S[0]] -= query[2]
                    query[2] = 0
        else:
            print(max(S) - min(S))

if __name__ == '__main__':
    main()