Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == n:
            break
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == n:
            ans = 1
        else:
            ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        j = i
        while j != 0:
            j = p[j]
            cnt += 1
        ans = max(ans, cnt)
    print(ans)
main()

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0,0)
    ans = 0
    for i in range(1, N+1):
        if P[i] < i:
            ans += 1
        else:
            ans += 1
            j = P[i]
            while j < i:
                ans += 1
                j = P[j]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        parent = P[i]
        while parent != 0:
            ans += 1
            parent = P[parent-1]
            if parent == 0:
                break
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans = max(ans, p[i-1])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        p1 = p[i-1]
        p2 = p[i]
        if p1 > p2:
            p1, p2 = p2, p1
        if p2 == n:
            ans = i
            break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    p = [0] + list(map(int,input().split()))
    ans = 0
    for i in range(1,n+1):
        ans = max(ans,depth(i,p))
    print(ans)

=======
Suggestion 9

def main():
    # 標準入力の受け取り
    n = int(input())
    p_list = list(map(int, input().split()))

    # 人数分の配列を作成
    parent_list = [0] * n

    # 親の人数分ループ
    for i in range(n - 1):
        # 親の人数分ループ
        for j in range(n - 1):
            # 親の人数分ループ
            if p_list[j] == i + 2:
                # 親の人数分ループ
                parent_list[i + 1] = parent_list[i] + 1

    # 結果を出力
    print(parent_list[n - 1])

=======
Suggestion 10

def get_input_lines():
    while True:
        try:
            line = input()
            yield line
        except EOFError:
            break
