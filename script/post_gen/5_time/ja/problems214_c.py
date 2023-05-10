Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    #n = int(input())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    #c = list(map(int, input().split()))
    #d = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [int(input()) for i in range(n)]
    n = int(i

=======
Suggestion 2

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0 for i in range(N)]
    for i in range(N):
        if i == 0:
            ans[i] = T[i]
        else:
            ans[i] = min(ans[i-1] + S[i-1], T[i])
    for i in range(N):
        print(ans[i])

=======
Suggestion 3

def solve(n, s, t):
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = t[i]
            continue
        ans[i] = min((ans[i-1] + s[i-1]) % t[i], t[i])
    return ans

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = solve(n, s, t)
print(*ans, sep='\n')

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    # 1. すぬけ君が初めて宝石をもらう時刻を求める
    # 2. 高橋君がすぬけ君に宝石を渡す時刻を求める
    # 3. 1.と2.の最大値が答え

    # 1. すぬけ君が初めて宝石をもらう時刻を求める
    # 1-1. すぬけ君が初めて宝石をもらう時刻を求める
    # 1-2. すぬけ君が初めて宝石をもらう時刻を求める
    # 1-3. すぬけ君が初めて宝石をもらう時刻を求める
    # 1-4. すぬけ君が初めて宝石をもらう時刻を求める

    # 2. 高橋君がすぬけ君に宝石を渡す時刻を求める
    # 2-1. 高橋君がすぬけ君に宝石を渡す時刻を求める
    # 2-2. 高橋君がすぬけ君に宝石を渡す時刻を求める
    # 2-3. 高橋君がすぬけ君に宝石を渡す時刻を求める
    # 2-4. 高橋君がすぬけ君に宝石を渡す時刻を求める

    # 3. 1.と2.の最大値が答え

    # 1

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(t[i])
        else:
            ans.append(min(ans[i-1]+s[i-1], t[i]))
    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    #print(N)
    #print(S)
    #print(T)

    # 1番目の人から順番に宝石をもらう時刻を求める
    # 1番目の人は高橋くんから宝石をもらう
    # 2番目の人は1番目から宝石をもらう
    # 3番目の人は2番目から宝石をもらう
    # 4番目の人は3番目から宝石をもらう
    # 5番目の人は4番目から宝石をもらう
    # 6番目の人は5番目から宝石をもらう
    # 7番目の人は6番目から宝石をもらう
    # 8番目の人は7番目から宝石をもらう
    # 1番目の人は8番目から宝石をもらう
    # 2番目の人は1番目から宝石をもらう
    # 3番目の人は2番目から宝石をもらう
    # 4番目の人は3番目から宝石をもらう
    # 5番目の人は4番目から宝石をもらう
    # 6番目の人は5番目から宝石をもらう
    # 7番目の人は6番目から宝石をもらう
    # 8番目の人は7番目から宝石をもらう
    # 1番目の人は8番目から宝石をもらう
    # 2番目の人は1番目から宝石をもらう
    # 3番目の人は2番目から宝石をもらう
    # 4番

=======
Suggestion 7

def get_input_data():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    return n, s_list, t_list

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = t[0]
    for i in range(1, n):
        ans[i] = min(ans[i-1] + s[i-1], t[i])
    for i in range(n):
        print(ans[i])
