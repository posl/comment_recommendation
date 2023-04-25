Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        if H[i-1] <= H[i]:
            count += 1
    print(count)

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    count = 0
    for h in H:
        if h >= max_h:
            max_h = h
            count += 1
    print(count)

main()

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))

    count = 1
    for i in range(1, n):
        if h[i] >= max(h[:i]):
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    M = [0] * N
    M[0] = H[0]
    for i in range(1, N):
        M[i] = max(M[i-1], H[i])
    print(sum([1 for i in range(N) if M[i] == H[i]]))

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        if all([H[j] <= H[i] for j in range(i)]):
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(n-1):
        if h[i] <= min(h[i+1:]):
            count += 1
    print(count)

=======
Suggestion 9

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

main()

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        else:
            if h[i] >= max(h[:i]):
                count += 1
    print(count)
