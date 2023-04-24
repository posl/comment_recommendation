Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        ans = 0
    else:
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
    print(ans)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    S = input()

    if S == S[::-1]:
        print(0)
        return

    cnt = 0
    for i in range(N):
        if S[i] != S[-i-1]:
            cnt += 1
    cnt //= 2

    if cnt == 1:
        print(min(A, B))
        return

    if cnt == 0:
        print(min(A, B*(N//2)))
        return

    print(min(A*(cnt-1)+B, A*cnt+B))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        print(ans)
        return
    for i in range(N):
        if S[i] != S[N-1-i]:
            ans = A
            break
    if ans == 0:
        ans = B
    print(ans)
    return

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if A < B:
        cnt = 1
        for i in range(1, N):
            if S[i] != S[i-1]:
                if S[i-1] == "a":
                    ans += A
                else:
                    ans += B
                cnt = 1
            else:
                cnt += 1
        if cnt % 2 == 1:
            ans += A
    else:
        ans = A * N
    print(ans)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()
    if A > B:
        print(0)
        return
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print(0)
            return
        print(A)
        return
    if S[:N//2] == S[N//2+1:]:
        print(0)
        return
    if S[:N//2] == S[N//2:]:
        print(B)
        return
    print(A)

=======
Suggestion 6

def main():
    N, A, B, S = read()
    ans = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            ans += min(A, B)
    print(ans)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    S = input()

    if N == 1:
        print(0)
        return

    # 総費用
    cost = 0

    # 現在の文字列
    now = S

    # 1文字ずつチェック
    for i in range(N//2):
        # 両端が同じなら何もしない
        if now[i] == now[N-1-i]:
            continue
        # 両端が異なるなら、A円払うかB円払うかを選択する
        else:
            # A円払う
            if A < B:
                cost += A
            # B円払う
            else:
                cost += B

    print(cost)

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    S = input()

    # 1文字目と最後の文字が同じかどうか
    is_same = True
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            is_same = False
            break

    if is_same:
        # 同じならば、A円払っても回文にならない
        print(0)
        return

    # 1文字目と最後の文字が違うならば、A円払っても回文にならない
    # ただし、1文字目と最後の文字以外が全て同じならば、A円払っても回文にならない
    is_same_except_1st_and_last = True
    for i in range(1, N // 2):
        if S[i] != S[N - 1 - i]:
            is_same_except_1st_and_last = False
            break

    if is_same_except_1st_and_last:
        # 1文字目と最後の文字以外が全て同じならば、A円払っても回文にならない
        # ただし、1文字目と最後の文字以外が全て同じならば、B円払っても回文にならない
        is_same_except_1st_and_last = True
        for i in range(1, N // 2):
            if S[i] != S[N - 2 - i]:
                is_same_except_1st_and_last = False
                break

    if is_same_except_1st_and_last:
        # 1文字目と最後の文字以外が全て同じならば、B円払っても回文にならない
        # ただし、1文字目と最後の文字以外が全て同じならば、A円払っても回文にならない
        is_same_except_1st_and_last = True
        for i in range(1, N // 2):
            if S[i] != S[N
