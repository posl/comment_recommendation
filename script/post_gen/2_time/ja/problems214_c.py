Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        for j in range(N):
            if ans[(i + j) % N] > ans[i] + S[i]:
                ans[(i + j) % N] = ans[i] + S[i]
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
        for j in range(i+1, N):
            if ans[j] < ans[j-1] + S[j-1]:
                ans[j] = ans[j-1] + S[j-1]
    for i in range(N):
        print(ans[i])

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [10**10] * N
    for i in range(N):
        for j in range(N):
            if ans[j] > T[i]:
                ans[j] = T[i]
                T[i] += S[j]
                break
    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = T

    for i in range(N):
        for j in range(N):
            if T[i] < T[j] and T[i] + S[i] < T[j]:
                ans[i] = T[j]
                break
        else:
            continue
        break

    for i in range(N):
        print(ans[i])

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    #処理
    ans = [0]*N
    for i in range(N):
        ans[i] = T[i]
        for j in range(N):
            if T[i] < ans[(i+j)%N]:
                ans[(i+j)%N] = T[i] + sum(S[(i+j)%N:(i+j)%N+j+1])

    #出力
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]

    # すぬけくんの情報
    # 0: 初めて宝石をもらう時刻
    # 1: 宝石をもらった時刻
    # 2: 宝石を渡した時刻
    # 3: 宝石を渡した相手の番号
    # 4: 宝石を渡した相手に渡した時刻
    # 5: 宝石を渡した相手に渡した相手の番号
    # 6: 宝石を渡した相手に渡した相手に渡した時刻
    # 7: 宝石を渡した相手に渡した相手に渡した相手の番号
    # 8: 宝石を渡した相手に渡した相手に渡した相手に渡した時刻
    # 9: 宝石を渡した相手に渡した相手に渡した相手に渡した相手の番号
    # 10: 宝石を渡した相手に渡した相手に渡した相手に渡した相手に渡した時刻
    # 11: 宝石を渡した相手に渡した相手に渡した相手に渡した相手に渡した相手の番号
    # 12: 宝石を渡した相手に渡した相手に渡した相手に渡した相手に渡した相手に渡した時刻
    # 13: 宝石を渡した相手に渡した相手に渡した相手に渡した相手に渡した相手に渡した相手の番号
    # 14: 宝石を渡した相手に

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # すぬけくんの番号をキー、初めて宝石を貰う時刻を値とする辞書を作成する。
    # すぬけくんは、初めに高橋くんから宝石を貰うので、
    # すぬけくんの初めて宝石を貰う時刻は、高橋くんから宝石を貰う時刻となる。
    # すぬけくんの初めて宝石を貰う時刻を初期値として、
    # すぬけくんの初めて宝石を貰う時刻を更新していく。
    # すぬけくんの初めて宝石を貰う時刻が、高橋くんから宝石を貰う時刻よりも後の場合は、
    # 高橋くんから宝石を貰う時刻を初めて宝石を貰う時刻とする。
    # すぬけくんの初めて宝石を貰う時刻が、高橋くんから宝石を貰う時刻よりも前の場合は、
    # すぬけくんの初めて宝石を貰う時刻をそのままとする。
    # すぬけくんの初めて宝石を貰う時刻が、高橋くんから宝石を貰う時刻と同じ場合は、
    # すぬけくんの初めて宝石を貰う時刻をそのままとする。
    # すぬけくんの初めて宝石を貰う

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    #Sの最大値
    maxS = max(S)
    #Tの最小値
    minT = min(T)
    #Tの最小値がSの最大値を超えたら、最小値を最大値にする
    if minT > maxS:
        minT = maxS
    #Tの最小値を超えるSの値を取り除く
    S = list(filter(lambda x: x > minT,S))
    #Tの最小値を超えるTの値を取り除く
    T = list(filter(lambda x: x > minT,T))
    #Tの最小値を超えるSの値の最小値
    minS = min(S)
    #Tの最小値を超えるSの値の最小値を超えるTの値を取り除く
    T = list(filter(lambda x: x > minS,T))
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値
    minT = min(T)
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値を超えるSの値を取り除く
    S = list(filter(lambda x: x > minT,S))
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値を超えるSの値の最小値
    minS = min(S)
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値を超えるSの値の最小値を超えるTの値を取り除く
    T = list(filter(lambda x: x > minS,T))
    #Tの最小値
