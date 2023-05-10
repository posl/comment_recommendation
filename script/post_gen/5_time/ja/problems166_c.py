Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [li

=======
Suggestion 2

def main():
    n,m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        if h[ab[i][0]-1] > h[ab[i][1]-1]:
            cnt += 1
        elif h[ab[i][0]-1] < h[ab[i][1]-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [0] * m
    for i in range(m):
        ab[i] = list(map(int, input().split()))
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1])
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1])
    print(h)
    print(ab)

    for i in range(m):
        if h[ab[i][0]-1] > h[ab[i][1]-1]:
            h[ab[i][0]-1] = 0
        elif h[ab[i][0]-1] < h[ab[i][1]-1]:
            h[ab[i][1]-1] = 0
        else:
            h[ab[i][0]-1] = 0
            h[ab[i][1]-1] = 0
    print(h)
    print(h.count(0))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if AB[j][0] == i+1 and H[i] <= H[AB[j][1]-1]:
                flag = False
                break
            elif AB[j][1] == i+1 and H[i] <= H[AB[j][0]-1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    ab_list = [list(map(int, input().split())) for _ in range(m)]

    max_h_list = [0] * n
    for ab in ab_list:
        a = ab[0] - 1
        b = ab[1] - 1
        max_h_list[a] = max(max_h_list[a], h_list[b])
        max_h_list[b] = max(max_h_list[b], h_list[a])

    ans = 0
    for i in range(n):
        if h_list[i] > max_h_list[i]:
            ans += 1

    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    good = [True] * N
    for i in range(M):
        if H[AB[i][0]-1] <= H[AB[i][1]-1]:
            good[AB[i][0]-1] = False
        if H[AB[i][1]-1] <= H[AB[i][0]-1]:
            good[AB[i][1]-1] = False
    print(good.count(True))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if AB[j][0] == i+1:
                if H[i] <= H[AB[j][1]-1]:
                    flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    answer = 0
    for i in range(n):
        check = True
        for j in range(m):
            if ab[j][0] == i+1:
                if h[i] <= h[ab[j][1]-1]:
                    check = False
                    break
        if check:
            answer += 1
    print(answer)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    #print(n, m)
    #print(h)
    #print(ab)

    # 良い展望台をカウントする
    # まず、良い展望台の候補を全てリストに入れる
    # 次に、良い展望台の候補から、良い展望台でないものを除外する
    # 良い展望台が残ったら、それをカウントする
    # 良い展望台の候補は、展望台番号のリストで良いかな？
    # それぞれの展望台について、それが良い展望台かどうかを判定する
    # 良い展望台でないものは、良い展望台の候補から除外する
    # どうやって除外する？
    # まず、良い展望台の候補のリストを作る
    # そのリストに、良い展望台でないものを除外する
    # 除外するには、良い展望台でないものの番号を、リストから削除する
    # それを、良い展望台の候補のリストについて、全ての展望台について行う
    # もし、良い展望台の候補のリストが変化しなくなったら、終了する
    # その時点で、良い展望台の候補のリストに残っている展望台の数が、良い展望台の数
    # 良い展望

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    good = [True] * N
    for a, b in AB:
        if H[a - 1] <= H[b - 1]:
            good[a - 1] = False
        if H[b - 1] <= H[a - 1]:
            good[b - 1] = False
    print(good.count(True))
