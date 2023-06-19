Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        flag = True
        for j in range(i):
            if h[j] >= h[i]:
                flag = False
        if flag:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    res = 0
    for i in range(N):
        if H[i] >= max_h:
            res += 1
            max_h = H[i]
    print(res)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        flag = True
        for j in range(i):
            if h[j] >= h[i]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    cnt = 0
    for i in range(n):
        if max <= h[i]:
            cnt += 1
        if max < h[i]:
            max = h[i]
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        for j in range(i):
            if H[j] > H[i]:
                break
        else:
            count += 1
    print(count)

=======
Suggestion 6

def problems124_b():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i] >= max(h[:i]):
            count += 1
    print(count)

problems124_b()

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        else:
            if max(h[:i]) <= h[i]:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        if i == 0 or max(h[0:i]) <= h[i]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 1
    for i in range(1,N):
        if max(H[:i]) <= H[i]:
            count += 1
    print(count)
