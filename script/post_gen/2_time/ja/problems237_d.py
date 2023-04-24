Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(*A)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(*A)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(' '.join([str(i) for i in A]))

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i + 1)
        else:
            A.append(i + 1)
    print(*A)

main()

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == "L":
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(*a)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == "L":
            L.append(i)
        else:
            R.append(i)
    A = [0]
    for i in range(N):
        if S[i] == "L":
            if len(L) > 0:
                A.insert(L[0], i+1)
                L.pop(0)
        else:
            if len(R) > 0:
                A.insert(R[0]+1, i+1)
                R.pop(0)
    print(*A)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'R':
            A.append(i+1)
        else:
            A.insert(0,i+1)
    print(*A)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N+1):
        if S[i-1] == 'L':
            A.insert(0, i)
        else:
            A.append(i)
    print(*A)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()

    # 0をN個入れたリストを作成
    A = [0] * (N + 1)

    # 0の位置を探す
    zero_index = A.index(0)

    # Sの各文字に対して処理
    for i, s in enumerate(S):
        # Lなら0の左にi+1を挿入
        if s == "L":
            A.insert(zero_index, i + 1)
        # Rなら0の右にi+1を挿入
        else:
            A.insert(zero_index + 1, i + 1)
        # 0の位置を探す
        zero_index = A.index(0)

    print(*A)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    # 0 は固定で最後に入れる
    # 1 から N までの数字をリストに入れる
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i + 1)
        else:
            A.append(i + 1)
    # 答えを出力
    print(*A)
