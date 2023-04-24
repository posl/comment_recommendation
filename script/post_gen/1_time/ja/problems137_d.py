Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    que = []
    for i in range(1, M + 1):
        while AB:
            a, b = AB.pop(0)
            if a <= i:
                heapq.heappush(que, -b)
            else:
                AB.append([a, b])
                break
        if que:
            ans -= heapq.heappop(que)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    import heapq
    q = []
    ans = 0
    for i in range(M):
        while AB and AB[0][0] == i+1:
            a, b = AB.pop(0)
            heapq.heappush(q, -b)
        if q:
            ans -= heapq.heappop(q)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    import heapq
    hq = []
    ans = 0
    for i in range(M):
        while len(AB) > 0 and AB[0][0] == i+1:
            heapq.heappush(hq, -AB[0][1])
            AB.pop(0)
        if len(hq) > 0:
            ans -= heapq.heappop(hq)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(M):
        if i < N:
            ans += AB[i][1]
        else:
            ans += 0
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]) # A_iでソート
    B = [0] # B_iを格納する
    for i in range(N):
        B.append(AB[i][1])
    B.sort(reverse=True) # B_iを大きい順にソート
    ans = 0
    for i in range(M):
        ans += B[i]
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    B = [0] * (M+1)
    for i in range(N):
        for j in range(M, AB[i][0]-1, -1):
            B[j] = max(B[j], B[j-AB[i][0]] + AB[i][1])
    print(B[M])

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    # A_i日後に報酬B_iが得られる日雇いアルバイトをA_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートする
    ab.sort(key=lambda x: x[1], reverse=True)
    # print(ab)
    # A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順にソートした結果を
    # 以下のように、A_i日後に報酬B_iが得られる日雇いアルバイトを報酬順に

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #報酬を最大化するためには、報酬の大きい順に日雇いアルバイトを請ける必要がある。
    #報酬の大きい順にソートする。
    AB.sort(key = lambda x: -x[1])
    #報酬の合計
    ans = 0
    #報酬の合計を最大化するためには、報酬の大きい順に日雇いアルバイトを請ける必要がある。
    #報酬の大きい順にソートした日雇いアルバイトを請けて、報酬を得る。
    for i in range(N):
        #日雇いアルバイトを請ける日
        day = AB[i][0]
        #報酬
        reward = AB[i][1]
        #日雇いアルバイトを請ける日が M 日後を含む日より後の場合は、日雇いアルバイトを請けない。
        if day > M:
            continue
        #日雇いアルバイトを請ける日が M 日後を含む日より前の場合は、日雇いアルバイトを請ける。
        #日雇いアルバイトを請けて、報酬を得る。
        ans += reward
        #日雇いアルバイトを請けた日が M 日後を含む日になる。
        M = day - 1
    #報酬の合計を出力する。
    print(ans)
