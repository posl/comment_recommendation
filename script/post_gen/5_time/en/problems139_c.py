Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    print(max_count)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))

    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)

    print(max_count)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    result = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            result = max(result, count)
            count = 0
    result = max(result, count)
    print(result)

=======
Suggestion 6

def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    maxcount = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            if maxcount < count:
                maxcount = count
            count = 0
    if maxcount < count:
        maxcount = count
    print(maxcount)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    m = 0
    t = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            t += 1
        else:
            m = max(t, m)
            t = 0
    m = max(t, m)
    print(m)

=======
Suggestion 9

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    max_count = 0
    count = 0
    for i in range(0, n-1):
        if heights[i] >= heights[i+1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 10

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    #print(N)
    #print(H)
    count = 0
    max_count = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            count = count + 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)
