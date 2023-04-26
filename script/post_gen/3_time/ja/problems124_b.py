Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if max(h[:i]) <= h[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        flag = True
        for j in range(i):
            if H[j] > H[i]:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(N):
        if max <= H[i]:
            count += 1
            max = H[i]

    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 1
    for i in range(1, N):
        if max(H[:i]) <= H[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if max <= h[i]:
            max = h[i]
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))

    count = 0
    max_height = 0
    for i in range(N):
        if H[i] >= max_height:
            count += 1
            max_height = H[i]

    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))

    count = 0
    max_height = 0
    for i in range(N):
        if max_height <= H[i]:
            count += 1
            max_height = H[i]

    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h_list[i-1] <= h_list[i]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_height = 0
    for h in H:
        if max_height <= h:
            count += 1
        max_height = max(max_height, h)
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if h_list[i] >= max:
            max = h_list[i]
            count += 1
    print(count)
