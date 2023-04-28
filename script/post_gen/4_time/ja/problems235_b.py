Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = h[0]
    for i in range(1,n):
        if ans <= h[i]:
            ans = h[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if h_list[i] < h_list[i+1]:
            ans = 0
        else:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = H[0]
    count = 0
    for i in range(1, N):
        if max_h <= H[i]:
            count += 1
            max_h = H[i]
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max_h = 0
    ans = 0
    for i in range(n):
        if max_h <= h[i]:
            ans += 1
            max_h = h[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))

    count = 0
    max = 0

    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
        else:
            count = 0
        if max < count:
            max = count

    print(max)

=======
Suggestion 7

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    
    count = 0
    for i in range(1, n):
        if h_list[i-1] < h_list[i]:
            count = 0
        else:
            count += 1
        if count >= 2:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        else:
            if h[i] >= h[i-1]:
                ans += h[i] - h[i-1]
    print(ans)
main()

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    if n == 2:
        print(max(h))
        return
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(cnt, ans)
    print(ans+1)
    return

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    #print(h)
    for i in range(n-1):
        if h[i+1] > h[i]:
            h[i+1] -= 1
    h.reverse()
    print(h[0])
