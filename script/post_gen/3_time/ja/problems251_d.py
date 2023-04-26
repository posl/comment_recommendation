Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    w = int(input())
    if w <= 2:
        print("NO")
    elif w % 2 == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1, 2)
    elif w == 2:
        print(2)
        print(1, 2)
    elif w == 1:
        print(1)
        print(1)
    else:
        print(3)
        print(1, 2, 3)

=======
Suggestion 3

def main():
    W = int(input())
    if W == 3:
        print(2)
        print(1,2)
    elif W == 2:
        print(2)
        print(1,1)
    elif W == 1:
        print(1)
        print(1)
    elif W == 0:
        print(0)
    else:
        print(3)
        print(1,2,3)

=======
Suggestion 4

def main():
    W = int(input())
    if W % 2 == 0:
        print(W // 2)
        for i in range(W // 2):
            print(2)
    else:
        print(W // 2 + 1)
        for i in range(W // 2):
            print(2)
        print(1)

=======
Suggestion 5

def main():
    W = int(input())
    if W <= 2:
        print(1)
        print(W)
    elif W <= 4:
        print(2)
        print(1, W-1)
    else:
        print(3)
        if W % 2 == 0:
            print(W//2, W//2)
        else:
            print(W//2, W//2+1)

=======
Suggestion 6

def main():
    w = int(input())
    if w <= 2:
        print('NO')
    elif w % 2 == 1:
        print('NO')
    else:
        print('YES')

=======
Suggestion 7

def solve():
    W = int(input())
    if W <= 2:
        print("NO")
    elif W % 2 == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 8

def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1, 2)
        return
    print(3)
    if w % 2 == 0:
        print(w // 2, w // 2, 2)
    else:
        print(w // 2, w // 2 + 1, 1)

=======
Suggestion 9

def solve(W):
    N = 300
    A = [0] * N
    A[0] = 1
    A[1] = 2
    A[2] = 3
    if W <= 3:
        return A[0:W]
    else:
        for i in range(3, N):
            A[i] = A[i - 1] + A[i - 2] + A[i - 3]
            if A[i] > W:
                return A[0:i]
        return A[0:N]
