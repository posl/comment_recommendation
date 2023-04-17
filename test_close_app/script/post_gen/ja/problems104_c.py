Synthesizing 10/10 solutions

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
        score = 0
        count = 0
        for j in range(D):
            if i >> j & 1:
                score += (j + 1) * 100 * p[j] + c[j]
                count += p[j]
        if score < G:
            for j in range(D - 1, -1, -1):
                if i >> j & 1 == 0:
                    for k in range(p[j]):
                        score += (j + 1) * 100
                        count += 1
                        if score >= G:
                            ans = min(ans, count)
                            break
                    break
        else:
            ans = min(ans, count)
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        cnt = 0
        sum = 0
        for j in range(D):
            if i & (1 << j):
                cnt += p[j]
                sum += p[j] * 100 * (j + 1) + c[j]
        if sum >= G:
            ans = min(ans, cnt)
        else:
            for k in range(D):
                if i & (1 << k):
                    continue
                else:
                    for l in range(p[k]):
                        sum += 100 * (k + 1)
                        cnt += 1
                        if sum >= G:
                            ans = min(ans, cnt)
                            break
                    break
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for bit in range(1 << D):
        s = 0
        num = 0
        for i in range(D):
            if bit & (1 << i):
                s += (i + 1) * 100 * p[i] + c[i]
                num += p[i]
        if s >= G:
            ans = min(ans, num)
            continue
        for i in range(D - 1, -1, -1):
            if bit & (1 << i):
                continue
            for j in range(p[i]):
                if s >= G:
                    break
                s += (i + 1) * 100
                num += 1
            break
        ans = min(ans, num)
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        a, b = map(int, input().split())
        p.append(a)
        c.append(b)
    # print(D, G, p, c)

    # 総合スコアを G 点以上にするために解く必要のある最小の問題数
    min_num =

=======

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    #print(D, G, p, c)
    ans = 100000000
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
            for j in reversed(range(D)):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    score += 100 * (j + 1)
                    count += 1
                break
        ans = min(ans, count)
    print(ans)

=======

def main():
    d,g=map(int,input().split())
    p=[0]*d
    c=[0]*d
    for i in range(d):
        p[i],c[i]=map(int,input().split())
    ans=10**9
    for i in range(2**d):
        sum=0
        cnt=0
        for j in range(d):
            if (i>>j)&1:
                sum+=100*(j+1)*p[j]+c[j]
                cnt+=p[j]
        if sum<g:
            for j in range(d):
                if (i>>j)&1:
                    continue
                for k in range(p[j]):
                    if sum<g:
                        sum+=100*(j+1)
                        cnt+=1
                    else:
                        break
        if sum>=g:
            ans=min(ans,cnt)
    print(ans)
main()

=======

def main():
    # 入力
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    # 処理
    # 総合スコアを G 点以上にすることは可能である
    # なので、100点問題を1問解くときの総合スコアを求める
    # 100点問題を1問解くときの総合スコアを、100点問題を2問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点問題を3問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点問題を4問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点問題を5問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点問題を6問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点問題を7問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点問題を8問解くときの総合スコアに加える
    # 100点問題を1問解くときの総合スコアを、100点

=======

def main():
    D, G = map(int, input().split())
    #print(D, G)
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    #print(p)
    #print(c)
    ans = 0
    #print("ans = ", ans)
    ans = D * 100
    #print("ans = ", ans)
    for i in range(D):
        ans = min(ans, solve(D, G, p, c, i))
        #print("ans = ", ans)
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    # print(D, G)
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    # print(p)
    # print(c)

    ans = 0
    for i in range(D):
        ans += p[i]
    # print(ans)

    for i in range(D):
        if (100 * (i + 1) * p[i] + c[i]) >= G:
            ans = min(ans, i + 1)
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for i in range(D)]

    # 1問目から順に解いていく
    # 解いた問題数をカウントする
    # 解いた問題数が最小のものを出力する
    # 解いた問題数が最小のものが複数ある場合は、解いた問題数が多いものを出力する
    # 解いた問題数が最小のものが複数あり、解いた問題数が多いものも複数ある場合は、
    # 解いた問題数が多いもののうち、コンプリートボーナスの総額が少ないものを出力する

    # 1問目から順に解いていく
    # 解いた問題数をカウントする
    # 解いた問題数が最小のものを出力する
    # 解いた問題数が最小のものが複数ある場合は、解いた問題数が多いものを出力する
    # 解いた問題数が最小のものが複数あり、解いた問題数が多いものも複数ある場合は、
    # 解いた問題数が多いもののうち、コンプリートボーナスの総額が少ないものを出力する

    # 1問目から順に解いていく
    # 解いた問題数をカウントする
    # 解いた問題数が最小のものを出力する
    # 解いた問題数が最小のものが複数ある場合は、解いた問題数が多いものを出力する
    # 解い
