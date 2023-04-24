Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    for t, k in query:
        t %= (A + B + C)
        for _ in range(t):
            if S[k - 1] == "A":
                k = (k - 1) % B + A + 1
            elif S[k - 1] == "B":
                k = (k - 1) % C + A + B + 1
            else:
                k = (k - 1) % A + 1
        print(S[k - 1])

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(s[(k - 1) % len(s)])
        elif t % 3 == 1:
            if s[(k - 1) % len(s)] == 'A':
                print('B')
            elif s[(k - 1) % len(s)] == 'B':
                print('C')
            elif s[(k - 1) % len(s)] == 'C':
                print('A')
        elif t % 3 == 2:
            if s[(k - 1) % len(s)] == 'A':
                print('C')
            elif s[(k - 1) % len(s)] == 'B':
                print('A')
            elif s[(k - 1) % len(s)] == 'C':
                print('B')

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    tki = []
    for _ in range(q):
        t, k = map(int, input().split())
        tki.append([t, k])
    for t, k in tki:
        print(solve(s, t, k))

=======
Suggestion 4

def solve():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        k -= 1
        for j in range(t):
            if s[k] == 'A':
                k //= 3
            elif s[k] == 'B':
                k = (k+len(s))//3
            else:
                k = (k+2*len(s))//3
        print(s[k])

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    s_list = list(s)
    a = s_list.count("A")
    b = s_list.count("B")
    c = s_list.count("C")
    for i in range(q):
        ti, ki = map(int, input().split())
        if ti % 3 == 1:
            if ki <= a:
                print("A")
            elif ki <= a + b:
                print("B")
            else:
                print("C")
        elif ti % 3 == 2:
            if ki <= b:
                print("B")
            elif ki <= a + b:
                print("C")
            else:
                print("A")
        else:
            if ki <= c:
                print("C")
            elif ki <= a + c:
                print("A")
            else:
                print("B")

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        # S = s
        # for i in range(t):
        #     S = S.replace('A', 'BC').replace('B', 'CA').replace('C', 'AB')
        # print(S[k-1])
        # ここから解説
        # 0回置換したときのsの各文字の置換後の文字数
        a, b, c = s.count('A'), s.count('B'), s.count('C')
        # 置換回数tに対して、各文字が何回置換されるか
        a_t = t % 3 * a
        b_t = t % 3 * b
        c_t = t % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t2 = (t // 3) % 3 * a
        b_t2 = (t // 3) % 3 * b
        c_t2 = (t // 3) % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t3 = (t // 9) % 3 * a
        b_t3 = (t // 9) % 3 * b
        c_t3 = (t // 9) % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t4 = (t // 27) % 3 * a
        b_t4 = (t // 27) % 3 * b
        c_t4 = (t // 27) % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t5 = (t // 81) % 3 * a
        b_t5 = (t // 81) % 3 * b

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    tki = [list(map(int, input().split())) for _ in range(q)]
    c = s.count('C')
    for i in range(q):
        t = tki[i][0]
        k = tki[i][1]
        if t % 3 == 0:
            if k <= len(s) - c:
                print(s[k - 1])
            else:
                print(s[k + c - len(s) - 1])
        elif t % 3 == 1:
            if k <= c:
                print(s[len(s) - k])
            else:
                print(s[k - c - 1])
        else:
            if k <= len(s) - c:
                print(s[k + c - 1])
            else:
                print(s[k - len(s) + c - 1])

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    # S の 1 文字目から i 文字目までの A,B,C の個数を格納する配列
    # A[i] = S[0:i+1] の A の個数
    # B[i] = S[0:i+1] の B の個数
    # C[i] = S[0:i+1] の C の個数
    A = [0] * (len(S) + 1)
    B = [0] * (len(S) + 1)
    C = [0] * (len(S) + 1)
    for i in range(len(S)):
        if S[i] == "A":
            A[i + 1] = A[i] + 1
            B[i + 1] = B[i]
            C[i + 1] = C[i]
        elif S[i] == "B":
            A[i + 1] = A[i]
            B[i + 1] = B[i] + 1
            C[i + 1] = C[i]
        else:
            A[i + 1] = A[i]
            B[i + 1] = B[i]
            C[i + 1] = C[i] + 1

    for _ in range(Q):
        t, k = map(int, input().split())
        # S^{(t)} の先頭から k 文字目を出力
        # S^{(t)} の先頭から k 文字目の A,B,C の個数を求める
        # S^{(t)} の先頭から k 文字目の A,B,C の個数のうち最大のものを出力する
        # この処理を Q 回行う
        a = A[k] + (A[-1] - A[k]) * (t % 3 == 1) + (B[-1] - B[k]) * (t % 3 == 2) + (C[-1] - C[k]) * (t % 3 == 0)
        b = B[k] + (A[-1] - A[k]) * (t % 3 == 2
