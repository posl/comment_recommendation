Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            ans += 1
            max_h = h[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    H_max = 0
    ans = 0
    for h in H:
        if h >= H_max:
            ans += 1
            H_max = h
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1

    for i in range(1, N):
        if H[i] >= max(H[:i]):
            count += 1

    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            c += 1
    print(c)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if all(h[i] >= h[j] for j in range(i)):
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    # input
    N = int(input())
    Hs = list(map(int, input().split()))

    # compute
    ans = 1
    for i in range(1, N):
        if Hs[i-1] <= Hs[i]:
            ans += 1

    # output
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if H[i] >= max(H[i:]):
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if H[i] >= max(H[i:]):
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    visible = 0
    max_height = 0
    for i in range(0, N):
        if H[i] >= max_height:
            visible += 1
            max_height = H[i]
    print(visible)

=======
Suggestion 10

def main():
    # read the input
    N = int(input())
    H = list(map(int, input().split()))
    
    # initialize the counter
    count = 0
    
    # loop through the list of heights
    for i in range(N):
        # check if the current height is the highest
        if H[i] == max(H[:i+1]):
            # if so, increment the counter
            count += 1
    
    # print the result
    print(count)
