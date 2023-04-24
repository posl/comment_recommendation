Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i+1] += 1
        if H[i] > H[i+1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        if H[i] > H[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N-1):
        if H[i] - H[i+1] > 1:
            print('No')
            return
        elif H[i] - H[i+1] == 1:
            H[i+1] += 1
    print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    H.append(0)
    for i in range(N):
        if H[i] < H[i + 1]:
            H[i + 1] -= 1
        elif H[i] > H[i + 1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))

    if N == 1:
        print("Yes")
        return

    for i in range(N-1):
        if H[i] > H[i+1]:
            print("No")
            return
        elif H[i] == H[i+1]:
            continue
        elif H[i] < H[i+1]:
            H[i+1] -= 1

    print("Yes")

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] - H[i - 1] >= 2:
            print("No")
            return
        elif H[i] - H[i - 1] == 1:
            H[i] -= 1
    print("Yes")

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N-1):
        if H[i+1] < H[i]:
            H[i+1] += 1

    if H == sorted(H):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] >= H[i - 1]:
            continue
        elif H[i] == H[i - 1] - 1:
            H[i] += 1
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))
    # ここに処理を書く
    for i in range(N-1):
        if H[i] > H[i+1]:
            print("No")
            exit()
        elif H[i] == H[i+1]:
            pass
        else:
            H[i+1] -= 1
    print("Yes")
