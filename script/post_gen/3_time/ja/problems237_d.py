Synthesizing 10/10 solutions (Duplicates hidden)

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
Suggestion 4

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(*a)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = [0]
    for i in range(n):
        if s[i] == "L":
            ans.insert(0, i+1)
        else:
            ans.append(i+1)
    print(*ans)

=======
Suggestion 6

def main():
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
Suggestion 7

def solve():
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
Suggestion 8

def main():
    N = int(input())
    S = input()
    # N = 5
    # S = "LRRLR"
    # N = 7
    # S = "LLLLLLL"
    A = [0]
    for i in range(1,N+1):
        if S[i-1] == "L":
            A.insert(0,i)
        else:
            A.append(i)
    print(" ".join(map(str,A)))

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    # 0を含めた数列の長さ
    l = n + 1
    a = [0] * l
    # 0の位置
    zero = 0
    for i in range(n):
        if s[i] == "L":
            a[zero] = i + 1
            zero -= 1
        else:
            a[zero + 1] = i + 1
            zero += 1
    print(*a)
