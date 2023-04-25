Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    n = len(s)
    c = 0
    for i in range(n):
        if s[i] == 'X':
            c += 1
        else:
            break
    for i in reversed(range(n)):
        if s[i] == 'X':
            c += 1
        else:
            break
    if c == n:
        print(min(n, k + n))
    else:
        print(min(n, c + 2 * k))

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == '.':
            break
        ans += 1
    for i in range(N-1, -1, -1):
        if S[i] == '.':
            break
        ans += 1
    if ans >= N:
        print(N)
        return
    for i in range(N):
        if S[i] == '.':
            break
    for j in range(N-1, -1, -1):
        if S[j] == '.':
            break
    if S[i] == S[j]:
        ans += 1
    ans += 2 * K
    print(min(ans, N))

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    if len(S) == max_count:
        print(max_count)
    elif max_count + K >= len(S):
        print(len(S))
    else:
        print(max_count + 2 * K + 1)

=======
Suggestion 4

def main():
    s = input()
    k = int(input())

    #s = 'XX...X.X.X.'
    #k = 2

    #s = 'XXXX'
    #k = 200000

    #s = 'X...X'
    #k = 1

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 3

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 0

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 1

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 2

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 4

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 5

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 6

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 7

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 8

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 9

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 10

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 11

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 12

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 13

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 14

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 15

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 16

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 17

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 18

    #s = 'X.XXXXXXX.X.X.XXX'
    #k = 19

    #s = 'X.XXXXXXX.X.X.XXX'
    #k =

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    N = len(S)
    X = 0
    for i in range(N):
        if S[i] == 'X':
            X += 1
    Y = N - X
    if Y <= K:
        print(N)
    else:
        L = []
        for i in range(N):
            if S[i] == '.':
                L.append(i)
        L.append(N)
        M = len(L)
        ans = 0
        for i in range(M - 1):
            ans = max(ans, L[i + 1] - L[i])
        print(ans - 1)

=======
Suggestion 6

def main():
    S, K = input().split()
    K = int(K)
    S = S.replace('.', 'X')
    print(max([len(x) for x in S.split('X')]) + min(K, S.count('.')))

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    S = S.replace('.', 'X')
    S = S.replace('X', 'X.')
    S = S.split('.')
    S.sort(key=len, reverse=True)
    print(S[0].count('X'))

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0

    # 連続するXの数を数える
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)

    # 連続するXの数がK以下なら、全ての.をXに変える
    if ans <= K:
        ans = N
    # 連続するXの数がKより大きいなら、
    # 連続するXの数がK+1以上の部分を全てXに変える
    else:
        ans = 0
        cnt = 0
        for i in range(N):
            if S[i] == 'X':
                cnt += 1
            else:
                if cnt >= K + 1:
                    ans += cnt - K
                cnt = 0
        if cnt >= K + 1:
            ans += cnt - K

    print(ans)

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    N = len(S)
    S = S.replace('.','X')
    if K == 0:
        print(S)
        return
    if S[0] == 'X':
        C = 1
        for i in range(1,N):
            if S[i] == 'X':
                C += 1
            else:
                break
        if C >= K:
            print(C)
            return
        else:
            K -= C
    if S[-1] == 'X':
        C = 1
        for i in range(N-2,-1,-1):
            if S[i] == 'X':
                C += 1
            else:
                break
        if C >= K:
            print(C)
            return
        else:
            K -= C
    C = 0
    for i in range(1,N-1):
        if S[i] == 'X':
            C += 1
        else:
            C = 0
        if C >= K:
            print(C)
            return
    print('0')

=======
Suggestion 10

def main():
    s = input()
    k = int(input())
    n = len(s)
    s += '.'

    # Find the maximum number of consecutive Xs
    # in the string by replacing at most K dots.
    max_x = 0
    for i in range(n):
        if s[i] == '.':
            j = i + 1
            while s[j] == '.':
                j += 1
            max_x = max(max_x, j - i)

    # Find the maximum number of consecutive Xs
    # in the string by replacing at most K dots.
    max_x = 0
    for i in range(n):
        if s[i] == '.':
            j = i + 1
            while s[j] == '.':
                j += 1
            max_x = max(max_x, j - i)

    # If K is greater than or equal to the number of dots,
    # we can replace all dots with Xs.
    if k >= s.count('.'):
        print(n)
        return

    # If there is a dot in the string,
    # we can replace all dots with Xs.
    if s.count('.') > 0:
        print(n)
        return

    # If there is no dot in the string,
    # we cannot replace any dots with Xs.
    print(max_x)
