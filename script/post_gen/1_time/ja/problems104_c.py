Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = float("inf")
    for i in range(2 ** D):
        total = 0
        cnt = 0
        for j in range(D):
            if (i >> j) & 1:
                total += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if total < G:
            for j in range(D - 1, -1, -1):
                if not ((i >> j) & 1):
                    for k in range(p[j]):
                        if total >= G:
                            break
                        total += 100 * (j + 1)
                        cnt += 1
                    break
        if total >= G:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(1<<D):
        score = 0
        cnt = 0
        for j in range(D):
            if (i>>j)&1:
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
        if score < G:
            for j in reversed(range(D)):
                if (i>>j)&1:
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    score += 100*(j+1)
                    cnt += 1
                break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(p)
    #print(c)
    #print(D, G)
    min_num = 1000
    for i in range(2**D):
        sum_score = 0
        num = 0
        for j in range(D):
            if ((i >> j) & 1):
                sum_score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if sum_score >= G:
            if min_num > num:
                min_num = num
        else:
            for j in range(D):
                if ((i >> j) & 1) == 0:
                    for k in range(p[j]):
                        sum_score += 100 * (j + 1)
                        num += 1
                        if sum_score >= G:
                            if min_num > num:
                                min_num = num
                            break
                    break
    print(min_num)

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        score = 0
        count = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                count += p[j]
        if score >= G:
            ans = min(ans, count)
        else:
            for j in range(D - 1, -1, -1):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    score += 100 * (j + 1)
                    count += 1
                    if score >= G:
                        ans = min(ans, count)
                        break
                break
    print(ans)

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    P = [0] * D
    C = [0] * D
    for i in range(D):
        P[i], C[i] = map(int, input().split())
    ans = 0
    for i in range(2 ** D):
        score = 0
        count = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * P[j] + C[j]
                count += P[j]
        if score >= G:
            ans = count
            break
        for j in range(D):
            if (i >> j) & 1:
                continue
            for k in range(P[j] - 1):
                if score >= G:
                    break
                score += 100 * (j + 1)
                count += 1
            if score >= G:
                ans = count
                break
        if score >= G:
            break
    print(ans)

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_, c_ = map(int, input().split())
        p.append(p_)
        c.append(c_)

    # 最大値
    max = 0
    for i in range(D):
        max += 100 * (i + 1) * p[i] + c[i]

    # 最小値
    min = 0
    for i in range(D):
        min += 100 * (i + 1) * p[i]

    # 最大値を超える
    if G > max:
        print(-1)
        return

    # 最小値を超えない
    if G < min:
        print(0)
        return

    # 最小値を超える
    if G == min:
        print(D)
        return

    # 最大値を超えない
    if G == max:
        print(D)
        return

    # 最小値を超える
    if G > min:
        # 超える問題の番号
        over = 0
        for i in range(D):
            if 100 * (i + 1) * p[i] + c[i] >= G:
                over = i
                break

        # 超える問題の数
        cnt = 0
        for i in range(over):
            cnt += p[i]

        # 超える問題の数
        cnt += (G - 100 * (over + 1) * p[over] - c[over]) // (100 * (over + 1)) + 1

        print(cnt)
        return

main()

=======
Suggestion 7

def main():
    #入力
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(D, G, p, c)

    #解く問題数の最小値を求める
    ans = 1000000
    for bit in range(1 << D):
        sum = 0
        cnt = 0
        max = 0
        for i in range(D):
            if bit & (1 << i):
                sum += (i + 1) * 100 * p[i] + c[i]
                cnt += p[i]
            else:
                max = i
        if sum < G:
            for j in range(p[max]):
                sum += (max + 1) * 100
                cnt += 1
                if sum >= G:
                    break
        if sum >= G:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    # input
    D, G = map(int, input().split())
    p, c = [], []
    for _ in range(D):
        p_, c_ = map(int, input().split())
        p.append(p_)
        c.append(c_)
    # compute
    min_num = 10**9
    for i in range(2**D):
        score = 0
        num = 0
        for j in range(D):
            if (i>>j)&1:
                score += 100*(j+1)*p[j] + c[j]
                num += p[j]
        if score < G:
            for j in range(1, p[D-1]+1):
                if score >= G:
                    break
                score += 100*(D-1)
                num += 1
        if score >= G:
            min_num = min(min_num, num)
    # output
    print(min_num)

=======
Suggestion 9

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p.append(list(map(int, input().split())))
    for i in range(D):
        c.append(p[i][1] + p[i][0] * 100)
    cnt = 0
    for i in range(D):
        cnt += p[i][0]
    for i in range(D):
        if G < c[i]:
            for j in range(p[i][0]):
                if G < (j + 1) * 100 * (i + 1):
                    cnt = min(cnt, j + 1)
                    break
            break
        else:
            G -= c[i]
    if G > 0:
        cnt = min(cnt, cnt - G // (100 * (i + 1)))
    print(cnt)

=======
Suggestion 10

def main():
    #入力
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    #最小値を求める
    min = 10000
    for i in range(2 ** D):
        #2進数に変換
        b = format(i, 'b')
        #0埋め
        b = b.zfill(D)
        #print(b)
        #問題数
        num = 0
        #合計点
        sum = 0
        #最後の問題を解く
        last = -1
        #print(b)
        for j in range(D):
            #print(b[j])
            #print(b[j] == '1')
            if b[j] == '1':
                num += pc[j][0]
                sum += pc[j][0] * 100 * (j + 1) + pc[j][1]
            else:
                last = j
        #print(sum)
        #print(num)
        if sum < G:
            if last >= 0:
                for k in range(pc[last][0]):
                    sum += 100 * (last + 1)
                    num += 1
                    if sum >= G:
                        break
        if sum >= G:
            if num < min:
                min = num
    print(min)
