Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(N):
        P[i] -= 1

    ans = -10 ** 18
    for i in range(N):
        score = 0
        visited = [False] * N
        visited[i] = True
        score += C[i]
        j = P[i]
        while not visited[j]:
            visited[j] = True
            score += C[j]
            j = P[j]
        if score <= 0:
            continue
        loop = 0
        k = P[j]
        while k != j:
            loop += 1
            k = P[k]
        loop += 1
        #print(i, score, loop)
        if K < loop:
            continue
        score *= (K - loop) // loop
        k = P[j]
        while k != j:
            score += C[k]
            k = P[k]
        score += C[j]
        ans = max(ans, score)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(N):
        P[i] -= 1
    ans = -10**10
    for i in range(N):
        j = i
        score = 0
        cnt = 0
        loop = []
        while True:
            j = P[j]
            score += C[j]
            loop.append(C[j])
            cnt += 1
            if j == i:
                break
        if score <= 0:
            ans = max(ans, max(loop))
            continue
        if cnt > K:
            ans = max(ans, max(loop))
            continue
        tmp = score * (K // cnt)
        ans = max(ans, tmp)
        if K % cnt == 0:
            continue
        tmp += max(loop[:K % cnt])
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float("inf")
    for i in range(N):
        x = i
        tmp = 0
        tmp_list = []
        tmp_list.append(C[x])
        tmp += C[x]
        x = P[x]-1
        while x != i:
            tmp_list.append(C[x])
            tmp += C[x]
            x = P[x]-1
        if tmp > 0:
            tmp_list = tmp_list*(K//len(tmp_list))+tmp_list[:K%len(tmp_list)]
            tmp = tmp*(K//len(tmp_list))+tmp*(K%len(tmp_list))
        else:
            tmp_list = tmp_list[:K]
            tmp = tmp*(K//len(tmp_list))+tmp*(K%len(tmp_list))
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print(C)
    #print()
    #print()
    #print()

    # 1. 0 から始める場合
    # 2. 1 から始める場合
    # 3. 2 から始める場合
    # 4. 3 から始める場合
    # 5. 4 から始める場合
    # 6. 5 から始める場合
    # 7. 6 から始める場合
    # 8. 7 から始める場合
    # 9. 8 から始める場合
    # 10. 9 から始める場合
    # 11. 10 から始める場合
    # 12. 11 から始める場合
    # 13. 12 から始める場合
    # 14. 13 から始める場合
    # 15. 14 から始める場合
    # 16. 15 から始める場合
    # 17. 16 から始める場合
    # 18. 17 から始める場合
    # 19. 18 から始める場合
    # 20. 19 から始める場合
    # 21. 20 から始める場合
    # 22. 21 から始める場合
    # 23. 22 から始める場合
    # 24. 23 から始める場合
    # 25. 24 から始める場合
    # 26. 25 から始める場合
    # 27. 26 から始める場合
    # 28. 27 から始める場合
    # 29. 28 から始める場合

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        now = i
        tmp = []
        while True:
            now = p[now] - 1
            tmp.append(c[now])
            if now == i:
                break
        if len(tmp) < k:
            m = max(tmp)
            if m <= 0:
                continue
            tmp = tmp * (k // len(tmp))
            tmp += tmp[:k % len(tmp)]
        else:
            tmp = tmp[:k]
        s = sum(tmp)
        if s <= 0:
            ans = max(ans, max(tmp))
        else:
            ans = max(ans, s + (k // len(tmp) - 1) * max(0, max(tmp)))
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        cur = i
        score = 0
        cnt = 0
        path = []
        while cnt < k:
            cur = p[cur]-1
            path.append(c[cur])
            score += c[cur]
            cnt += 1
            if cur == i:
                break
        if cnt == k:
            ans = max(ans, score)
            continue
        if score <= 0:
            ans = max(ans, max(path))
            continue
        loop = (k-cnt)//len(path)
        rest = (k-cnt)%len(path)
        ans = max(ans, max(path)*loop+max(0, score)*loop+max(path[:rest]))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 9
    for i in range(N):
        score = 0
        cnt = 0
        j = i
        while cnt < K:
            score += C[j]
            j = P[j] - 1
            cnt += 1
            if j == i:
                break
        if cnt == K:
            ans = max(ans, score)
            continue
        m = 0
        j = i
        while j != P[j] - 1:
            m += C[j]
            j = P[j] - 1
        if m <= 0:
            ans = max(ans, score)
            continue
        score += m * ((K - cnt) // cnt)
        ans = max(ans, score)
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = -10**18
    for i in range(n):
        # i番目からスタートする
        # s: スコア
        # j: 移動回数
        s = 0
        j = 0
        # 現在地
        now = i
        # 現在地を通ったか
        passed = [0] * n
        passed[now] = 1

        while True:
            # 現在地から次の地点に移動
            now = p[now] - 1
            # 移動回数を加算
            j += 1
            # スコアを加算
            s += c[now]
            # 現在地を通ったことを記録
            passed[now] = 1

            # 現在地がスタート地点の場合
            if now == i:
                # 一周したのでループを抜ける
                break

            # 移動回数がk以下の場合
            if j <= k:
                # スコアの最大値を更新
                ans = max(ans, s)

        # 一周したので、移動回数がkを超えた場合
        if j > k:
            # 一周するまでのスコアの最大値を求める
            max_s = 0
            for i in range(n):
                if passed[i] == 0:
                    continue
                max_s += c[i]
            # 一周するまでのスコアの最大値が0以下の場合
            if max_s <= 0:
                continue
            # 一周するまでのスコアの最大値が0より大きい場合
            else:
                # 一周するまでのスコアの最大値を、k回の移動で一周するまでのスコアの最大値として計算

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    res = -10**18
    for i in range(N):
        now = i
        score = 0
        loop = []
        while True:
            now = P[now]
            score += C[now]
            loop.append(score)
            if now == i:
                break
        looplen = len(loop)
        if score <= 0:
            res = max(res, max(loop))
        else:
            res = max(res, max(loop) + (K//looplen)*score)
            res = max(res, max(loop[:K%looplen]) + (K//looplen)*score)
    print(res)
