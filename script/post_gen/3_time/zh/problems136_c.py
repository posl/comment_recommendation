Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(n-1):
        if h[i] - h[i+1] > 1:
            print("No")
            return
        elif h[i] - h[i+1] == 1:
            h[i+1] += 1
    print("Yes")

=======
Suggestion 2

def main():
    # 读入数据
    N = int(input())
    H = list(map(int, input().split()))

    # 从右向左检查
    for i in range(N - 1, 0, -1):
        if H[i] < H[i - 1]:
            H[i - 1] -= 1

    # 输出结果
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    h = [int(i) for i in input().split()]

    for i in range(1, n):
        if h[i] > h[i-1]:
            h[i] -= 1

    for i in range(1, n):
        if h[i] < h[i-1]:
            print("No")
            return

    print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))

    for i in range(1, n):
        if h[i] > h[i-1]:
            h[i] -= 1
    for i in range(1, n):
        if h[i] < h[i-1]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
        elif h[i] > h[i+1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1, 0, -1):
        if h[i] < h[i - 1]:
            h[i - 1] -= 1
        if h[i] < h[i - 1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def solve(n, h):
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            return False
    return True

n = int(input())
h = list(map(int, input().split()))

=======
Suggestion 8

def main():
    N = int(input())
    H = [int(i) for i in input().split(" ")]
    for i in range(1,N):
        if H[i] > H[i-1]:
            H[i] -= 1
    for i in range(1,N):
        if H[i] < H[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(n-1):
        if h[i] - h[i+1] > 1:
            print('No')
            exit()
        elif h[i] - h[i+1] == 1:
            h[i+1] += 1
    print('Yes')

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(n-1):
        if h[i] < h[i+1]:
            h[i+1] -= 1
        if h[i] < h[i+1]:
            print("No")
            return
    print("Yes")
