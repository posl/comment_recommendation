Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L = int(input())
    if L % 3 == 0:
        print((L / 3) ** 3)
    elif L % 3 == 1:
        print((L // 3 + 1) * (L // 3) * (L // 3))
    else:
        print((L // 3 + 1) * (L // 3 + 1) * (L // 3))

=======
Suggestion 2

def main():
    L = int(input())
    ans = 0
    for i in range(1, L):
        for j in range(1, L):
            for k in range(1, L):
                if i + j + k == L:
                    ans = max(ans, i * j * k)
    print(ans)

=======
Suggestion 3

def main():
    L = int(input())

    ans = 0
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            if i * j > L:
                break
            ans = max(ans, i * j * (L - i * j))

    print(ans)

=======
Suggestion 4

def main():
    L = int(input())
    if L % 3 == 0:
        print((L / 3) ** 3)
        return
    if L % 2 == 0:
        print((L / 2) ** 3 / 8)
        return
    else:
        print((L - 1) * (L - 2) * (L - 3) / 6)

=======
Suggestion 5

def main():
    # 入力
    L = int(input())

    # 処理
    if L % 3 == 0:
        ans = (L / 3) ** 3
    else:
        ans = (L // 3) ** 3
        ans = max(ans, (L // 3 + 1) ** 3)
        ans = max(ans, (L // 3) ** 3 * (L % 3))
        ans = max(ans, (L // 3 + 1) ** 3 * (L % 3))

    # 出力
    print(ans)

=======
Suggestion 6

def main():
    L = int(input())
    max_vol = 0
    for i in range(1,L):
        for j in range(1,L):
            k = L - i - j
            if k < 1:
                continue
            vol = i*j*k
            if vol > max_vol:
                max_vol = vol
    print(max_vol)

=======
Suggestion 7

def main():
    L = int(input())
    print((L/3)**3)

=======
Suggestion 8

def main():
    L = int(input())

    res = 0
    for i in range(1, L):
        for j in range(1, L):
            if i * j > L:
                break
            k = L - i * j
            res = max(res, i * j * k)

    print(res)

=======
Suggestion 9

def main():
    L = int(input())
    print(L ** 3 / 27)

=======
Suggestion 10

def main():
    L = int(input())
    #L = 3
    #L = 999
    #L
