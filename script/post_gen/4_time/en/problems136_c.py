Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            h[i + 1] -= 1
        if h[i] > h[i + 1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
        if h[i] > h[i+1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 4

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] < H[i-1]:
            H[i] += 1
    if sorted(H) == H:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i+1] - h[i] > 1:
            print("No")
            return
        elif h[i+1] - h[i] == 1:
            h[i+1] -= 1
    print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    flag = True
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        if h[i] > h[i + 1]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    for i in range(n-1):
        if h[i+1] - h[i] > 1:
            print("No")
            return
        elif h[i+1] - h[i] == 1:
            h[i+1] -= 1
    print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    H.reverse()
    for i in range(1, N):
        if H[i - 1] - H[i] > 1:
            print('No')
            return
        elif H[i - 1] - H[i] == 1:
            H[i] += 1
    print('Yes')
    return
