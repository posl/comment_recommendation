Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def get_input():
    n = int(input())
    h = list(map(int, input().split()))
    return n, h

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            cnt += 1
    print(cnt)
main()

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if h[i] >= max:
            count += 1
            max = h[i]
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    cnt = 0
    for i in range(n):
        for j in range(i):
            if h[i] < h[j]:
                break
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if max <= h[i]:
            count = count + 1
            max = h[i]
    print(count)
main()

=======
Suggestion 8

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    cnt = 1
    for i in range(1, n):
        flag = True
        for j in range(0, i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def problems124_b():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if max(h[:i+1]) == h[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))

    count = 1
    for i in range(1, N):
        for j in range(0, i):
            if H[j] > H[i]:
                break
            if j == i - 1:
                count += 1

    print(count)
