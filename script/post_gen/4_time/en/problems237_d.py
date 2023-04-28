Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'R':
            A.append(i+1)
        else:
            A.insert(0, i+1)
    print(*A)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "R":
            A.append(i+1)
        else:
            A.insert(0, i+1)
    print(*A)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i + 1)
        else:
            a.append(i + 1)
    print(' '.join(map(str, a)))

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i + 1)
        else:
            a.append(i + 1)
    print(*a)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1,N+1):
        if S[i-1] == 'L':
            A.insert(0,i)
        else:
            A.insert(len(A),i)
    print(' '.join(map(str,A)))
    return

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N + 1):
        if S[i - 1] == "L":
            A.insert(0, i)
        else:
            A.append(i)
    print(" ".join(map(str, A)))

=======
Suggestion 8

def solve():
    N = int(input())
    S = input()
    ans = [0]
    for i in range(N):
        if S[i] == 'L':
            ans.insert(0, i+1)
        else:
            ans.append(i+1)
    print(*ans)

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()

    # 0を配列の中央に配置
    A = [0]
    # 1からNまでの数字を順番に追加
    for i in range(1, N + 1):
        # Lの場合は配列の先頭に追加
        if S[i - 1] == "L":
            A.insert(0, i)
        # Rの場合は配列の末尾に追加
        else:
            A.append(i)
    print(*A)
