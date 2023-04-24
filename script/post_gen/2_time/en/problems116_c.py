Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if h[i] > h[i+1]:
            ans += h[i] - h[i+1]
            h[i+1] = h[i]
    return ans

print(solve())

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] == 0:
            continue
        ans += 1
        for j in range(i+1, N):
            if H[j] <= H[i]:
                H[j] = 0
            else:
                break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] == 0:
            continue
        ans += 1
        for j in range(i + 1, N):
            if H[j] > 0:
                H[j] -= 1
            else:
                break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, N):
        if h[i] > h[i - 1]:
            ans += h[i] - h[i - 1]
    print(ans + h[0])

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for h in H:
        ans += h
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            if h[i] > h[i-1]:
                ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            ans += max(0, h[i] - h[i-1])
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if H[i] > H[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    heights = list(map(int, input().split()))
    operations = 0
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            operations += heights[i-1] - heights[i]
            heights[i] = heights[i-1]
    print(operations)

=======
Suggestion 10

def   main (): 
     N   =   int ( input ()) 
     h   =   list ( map ( int ,   input (). split ())) 

     # 連続した区間を見つける
