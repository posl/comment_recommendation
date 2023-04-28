Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(C[i:i+K])))
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    s = set()
    for i in range(k):
        s.add(c[i])
    m = len(s)
    for i in range(k, n):
        s.remove(c[i-k])
        s.add(c[i])
        m = max(m, len(s))
    print(m)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    C = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = len(set(C[i:i+K]))
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    result = 0
    for i in range(N - K + 1):
        result = max(result, len(set(c[i:i + K])))
    print(result)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            ans = len(set(c[i:i+K]))
        else:
            if c[i-1] == c[i+K-1]:
                ans = max(ans, ans)
            else:
                ans = max(ans, len(set(c[i:i+K])))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    colors = set(c[:K])
    max_colors = len(colors)
    for i in range(1, N-K+1):
        colors.remove(c[i-1])
        colors.add(c[i+K-1])
        max_colors = max(max_colors, len(colors))
    print(max_colors)

=======
Suggestion 7

def  main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
    ans = len(d)
    for i in range(1, n-k+1):
        if d[c[i-1]] == 1:
            del d[c[i-1]]
        else:
            d[c[i-1]] -= 1
        if c[i+k-1] in d:
            d[c[i+k-1]] += 1
        else:
            d[c[i+k-1]] = 1
        ans = max(ans, len(d))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    color_list = list(map(int, input().split()))
    color_set = set(color_list)
    if len(color_set) <= K:
        print(len(color_set))
        return
    color_count = {}
    for i in range(K):
        if color_list[i] in color_count:
            color_count[color_list[i]] += 1
        else:
            color_count[color_list[i]] = 1
    max_num = len(color_count)
    for i in range(K, N):
        color_count[color_list[i - K]] -= 1
        if color_count[color_list[i - K]] == 0:
            del color_count[color_list[i - K]]
        if color_list[i] in color_count:
            color_count[color_list[i]] += 1
        else:
            color_count[color_list[i]] = 1
        max_num = max(max_num, len(color_count))
    print(max_num)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    # すでに見た色を保存するためのリスト
    seen = []
    # 今見ている連続するk個の色
    tmp = c[:k]
    # 今見ている連続するk個の色の中で最も多く出現する色の数
    ans = 0
    for i in range(k):
        if tmp[i] not in seen:
            seen.append(tmp[i])
            ans = max(ans, len(seen))
    for i in range(k, n):
        # 今見ている連続するk個の色の中で最も多く出現する色の数
        # 重複を許しているので、最大値はk
        if ans == k:
            break
        # 一番左の色を除く
        tmp = tmp[1:]
        # 新しく追加する色
        new_c = c[i]
        # 除いた色が新しく追加する色と違う場合
        if new_c not in tmp:
            # 除いた色がすでに見た色にある場合
            if new_c in seen:
                # 除いた色を新しく追加する色に置き換える
                tmp.append(new_c)
            # 除いた色がすでに見た色にない場合
            else:
                # 除いた色を新しく追加する色に置き換える
                tmp.append(new_c)
                # 除いた色を新しく追加する色に置き換えたので、
                # 今見ている連続するk個の色の中で最も多く出現する色の数を更新する
                ans = max(ans, len(seen) + 1)
        # 一番左の色を除いた場合、
        # 今見ている連続するk個
