def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(edges)
    #print(queries)
    #print()
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    #print(graph)
    #print()
    # DFS
    #https://atcoder.jp/contests/abc138/submissions/20751130
    #https://atcoder.jp/contests/abc138/submissions/20751320
    #https://atcoder.jp/contests/abc138/submissions/20751372
    #https://atcoder.jp/contests/abc138/submissions/20751489
    #https://atcoder.jp/contests/abc138/submissions/20751544
    #https://atcoder.jp/contests/abc138/submissions/20751691
    #https://atcoder.jp/contests/abc138/submissions/20751731
    #https://atcoder.jp/contests/abc138/submissions/20751844
    #https://atcoder.jp/contests/abc138/submissions/20751938
    #https://atcoder.jp/contests/abc138/submissions/20752042
    #https://atcoder.jp/contests/abc138/submissions/20752163
    #https://atcoder.jp/contests/abc138/submissions/20752260
    #https://atcoder.jp/contests/abc138/submissions/20752301
    #https://atcoder.jp/contests/abc138/submissions/20752354
    #https://atcoder.jp/contests/abc138/submissions/20752408
    #https://atcoder.jp/contests/abc138/submissions/20752449
    #https://atcoder.jp/contests/abc138/submissions/20752592
    #https://atcoder.jp/contests/abc138/submissions/20752644
    #https://atcoder.jp/
