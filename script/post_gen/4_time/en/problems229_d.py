Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    n = len(s)
    cnt = 0
    ans = 0
    for i in range(n):
        if s[i] == "X":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(min(n, ans + k * 2))

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    tmp = 0
    for i in range(n):
        if s[i] == 'X':
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(min(ans + k, n))

main()

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    N = len(S)
    i = 0
    ans = 0
    while i < N:
        if S[i] == 'X':
            i += 1
            continue
        j = i
        while j < N and S[j] == '.':
            j += 1
        ans = max(ans, j - i)
        i = j
    print(min(N, ans + 2 * K))

=======
Suggestion 4

def solve():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == "X":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    if ans + K >= N:
        print(N)
    else:
        print(ans + K + 1)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    if s.count('.') == 0:
        ans = n
    else:
        for i in range(n):
            if s[i] == '.':
                continue
            for j in range(i, n):
                if s[j] == '.':
                    continue
                if j - i + 1 <= k:
                    ans = max(ans, j - i + 1)
                else:
                    break
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    N = len(S)
    Xs = []
    for i in range(N):
        if S[i] == 'X':
            if i == 0 or S[i-1] != 'X':
                Xs.append(0)
            Xs[-1] += 1
    ans = 0
    for i in range(len(Xs)):
        ans += Xs[i]
        if K >= Xs[i]:
            K -= Xs[i]
            ans += K
            break
    print(ans)

main()

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    n = len(s)
    s = s.replace('.', '0')
    s = s.replace('X', '1')
    s = list(s)
    s = [int(i) for i in s]
    cumsum = [0]
    for i in range(n):
        cumsum.append(cumsum[i] + s[i])
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j - i <= ans:
                continue
            if cumsum[j] - cumsum[i] + k >= j - i:
                ans = max(ans, j - i)
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    s = s.replace('.', 'X')
    if len(s) <= k:
        print(len(s))
    else:
        print(s[:k].count('X') + s[k:].count('X') + 1)

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    s = s.replace('.', '')
    print(max(len(s) + min(k, len(s) - 1), len(s)))

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    N = len(S)

    # Sの中の連続した.の最大値を求める
    # 例えばS = XX...X.X.X.の場合、
    # 連続した.の最大値は2
    max_dot = 0
    tmp = 0
    for i in range(N):
        if S[i] == '.':
            tmp += 1
        else:
            max_dot = max(max_dot, tmp)
            tmp = 0
    max_dot = max(max_dot, tmp)

    # Sの中に連続した.が存在しない場合
    if max_dot == 0:
        print(min(N, K * 2 + 1))
        return

    # Sの中に連続した.が存在する場合
    # 連続した.をXに変換することで、
    # 連続したXの最大値は、連続した.の最大値 + K
    print(min(N, max_dot + K * 2))
