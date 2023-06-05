Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(raw_input())
    h = map(int, raw_input().split())
    cnt = 0
    for i in range(n):
        flag = True
        for j in range(i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print cnt

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if h[i] >= max:
            max = h[i]
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    count = 1
    for i in range(1,n):
        if h[i] >= max(h[:i]):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 5

def solution():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        flag = True
        for j in range(i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 6

def get_sea_view_count(h):
    count = 0
    for i in range(len(h)):
        if i == 0:
            count += 1
        else:
            if h[i] >= max(h[0:i]):
                count += 1
    return count

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if all(H[i] > H[j] for j in range(i)):
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        for j in range(i):
            if h[i] < h[j]:
                break
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def solution(h):
    count = 1
    for i in range(1, len(h)):
        if h[i] >= max(h[:i]):
            count += 1
    return count

=======
Suggestion 10

def main():
    # input
    N = int(input())
    H = [int(n) for n in input().split()]
    # print(N)
    # print(H)

    # count
    count = 0
    max = 0
    for i in range(N):
        if max <= H[i]:
            count += 1
        if max < H[i]:
            max = H[i]
    print(count)
