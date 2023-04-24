Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for _ in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            if query[1] in S:
                S.remove(query[1])
        else:
            if len(S) != 0:
                print(max(S)-min(S))

=======
Suggestion 2

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    S = Counter()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S[query[1]] += 1
        elif query[0] == 2:
            S[query[1]] = max(S[query[1]] - query[2], 0)
        else:
            print(max(S.keys()) - min(S.keys()))
    return

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    d = defaultdict(int)
    max_val = 0
    min_val = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d[query[1]] += 1
            if max_val == 0 and min_val == 0:
                max_val = query[1]
                min_val = query[1]
            else:
                max_val = max(query[1], max_val)
                min_val = min(query[1], min_val)
        elif query[0] == 2:
            if d[query[1]] <= query[2]:
                query[2] = d[query[1]]
            d[query[1]] -= query[2]
            if d[query[1]] == 0:
                del d[query[1]]
            if max_val == query[1]:
                if len(d) == 0:
                    max_val = 0
                    min_val = 0
                else:
                    max_val = max(d.keys())
            if min_val == query[1]:
                if len(d) == 0:
                    max_val = 0
                    min_val = 0
                else:
                    min_val = min(d.keys())
        else:
            print(max_val - min_val)

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    import heapq
    hq1 = []
    hq2 = []
    for a in A:
        if a[0] == 1:
            heapq.heappush(hq1, a[1])
            heapq.heappush(hq2, -a[1])
        elif a[0] == 2:
            c = a[2]
            for i in range(c):
                if hq1[0] == a[1]:
                    heapq.heappop(hq1)
                    break
            for i in range(c):
                if -hq2[0] == a[1]:
                    heapq.heappop(hq2)
                    break
        else:
            print(-hq2[0] - hq1[0])

=======
Suggestion 7

def main():
    from collections import Counter, deque
    Q = int(input())
    que = [list(map(int, input().split())) for _ in range(Q)]
    c = Counter()
    d = deque()
    for i in range(Q):
        if que[i][0] == 1:
            c[que[i][1]] += 1
            d.append(que[i][1])

        elif que[i][0] == 2:
            if c[que[i][1]] > 0:
                c[que[i][1]] -= 1
                if c[que[i][1]] == 0:
                    c.pop(que[i][1])
                d.append(que[i][1])

        else:
            while d:
                if c[d[0]] > 0:
                    break
                else:
                    d.popleft()

            while d:
                if c[d[-1]] > 0:
                    break
                else:
                    d.pop()

            print(c[d[-1]] - c[d[0]])

=======
Suggestion 8

def main():
    # 1. 入力
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(input().split())
    # 2. 3のクエリを処理するとき、 S が空でないことが保証される。
    # 3. 3のクエリに対する答えを順に改行区切りで出力せよ。
    # 4. 3のクエリを処理するとき、S は空でない。
    # 5. 3のクエリを処理するとき、S は空でない。
    # 6. 3のクエリを処理するとき、S は空でない。
    # 7. 3のクエリを処理するとき、S は空でない。
    # 8. 3のクエリを処理するとき、S は空でない。
    # 9. 3のクエリを処理するとき、S は空でない。
    # 10. 3のクエリを処理するとき、S は空でない。

    # 11. 3のクエリを処理するとき、S は空でない。
    # 12. 3のクエリを処理するとき、S は空でない。
    # 13. 3のクエリを処理するとき、S は空でない。
    # 14. 3のクエリを処理するとき、S は空でない。
    # 15. 3のクエリを処理するとき、S は空でない。
    # 16. 3のクエリを処理するとき、S は空でない。
    # 17. 3のクエリを処理するとき、S は空でない。
    # 18. 3のクエリを処理するとき

=======
Suggestion 9

def main():
    Q = int(input())
    # 1. 1のクエリを受け取ったとき
    # 2. 2のクエリを受け取ったとき
    # 3. 3のクエリを受け取ったとき
    # 4. その他のクエリを受け取ったとき
    # 5. 全てのクエリを受け取ったとき
    # 6. 入力を受け取ったとき
    # 7. 出力を行ったとき
    # 8. 最大値を出力したとき
    # 9. 最小値を出力したとき
    # 10. 1のクエリを受け取っているとき
    # 11. 2のクエリを受け取っているとき
    # 12. 3のクエリを受け取っているとき
    # 13. 1のクエリを受け取ったとき
    # 14. 2のクエリを受け取ったとき
    # 15. 3のクエリを受け取ったとき
    # 16. その他のクエリを受け取ったとき
    # 17. 全てのクエリを受け取ったとき
    # 18. 入力を受け取ったとき
    # 19. 出力を行ったとき
    # 20. 最大値を出力したとき
    # 21. 最小値を出力したとき
    # 22. 1のクエリを受け取っているとき
    # 23. 2のクエリを受け取っているとき
    # 24. 3のクエリを受け取っているとき
    # 25. 1のクエリを受け取

=======
Suggestion 10

def main():
    import sys
    import io
    import os
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    # この問題は、最大値と最小値を求める問題である。
    # これは、最大値と最小値をO(1)で求められるデータ構造を用いることで解くことができる。
    # この問題では、最大値と最小値を求めることができるsetを用いる。
    # ただし、setは重複を許さないため、重複を許すmultisetを用いる。
    # pythonにはmultisetはないため、defaultdictを用いて実装する。
    # defaultdictは、キーが存在しない場合に、デフォルト値を返すデータ構造である。
    # このデフォルト値は、初期化時に与えることができる。
    # 今回は、キーが存在しない場合に0を返すように設定する。
    # これにより、multisetのように扱うことができる。
    # また、multisetを用いると、最大値と最小値を求めることができる。
    # また、multisetは、要素の追加、削除がO(logN)でできる。
    # 今回の問題では、クエリ1は要素の追加、クエリ2は要素の削除、クエリ3は、最大値と最小値の差を出力する。
    # クエリ1の場合、要素を追加する。
    # クエリ2の場合、要素を削除する。
    # ただし、要素を削除する際には
