Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    count = 0
    for height in heights:
        if height >= k:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

=======
Suggestion 3

def get_input():
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    return n,k,h

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(len([x for x in h if x >= k]))

=======
Suggestion 5

def main():
    num, height = map(int, input().split())
    heights = list(map(int, input().split()))
    count = 0
    for h in heights:
        if h >= height:
            count += 1
    print(count)

=======
Suggestion 6

def get_input():
    #input_str = input()
    input_str = "4 150"
    input_list = input_str.split()
    n = int(input_list[0])
    k = int(input_list[1])
    #input_str = input()
    input_str = "150 140 100 200"
    input_list = input_str.split()
    h_list = []
    for i in range(n):
        h_list.append(int(input_list[i]))
    return n, k, h_list

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in h:
        if i >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if h[i] >= K:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    print(ans)
