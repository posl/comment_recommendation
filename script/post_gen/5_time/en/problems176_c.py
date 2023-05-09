Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    stools = [0] * N
    stools[0] = A[0]
    for i in range(1, N):
        stools[i] = max(stools[i-1], A[i])
    print(sum(stools) - sum(A))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            ans += a[i-1] - a[i]
            a[i] = a[i-1]
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    stools = [0] * N
    for i in range(N-1):
        if A[i+1] > A[i]:
            stools[i+1] = stools[i] + A[i+1] - A[i]
    print(sum(stools))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    ans = 0
    for i in range(n):
        if a[i] > max:
            max = a[i]
        else:
            ans += max - a[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1, -1, -1):
        if A[i] > ans:
            ans = A[i]
        else:
            ans = ans - 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_height = 0
    total_height = 0
    for i in range(N):
        if A[i] >= max_height:
            total_height += A[i] - max_height
            max_height = A[i]
        else:
            max_height = A[i]
    print(total_height)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    answer = 0
    for i in range(n):
        if a[i] >= max_height:
            max_height = a[i]
        else:
            answer += max_height - a[i]
    print(answer)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = a[0]
    stools = [0] * n
    for i in range(1, n):
        stools[i] = max_a - a[i]
        if a[i] > max_a:
            max_a = a[i]
    print(sum(stools))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    total_height = 0
    for i in range(n):
        if(a[i] > max_height):
            max_height = a[i]
        total_height += max_height - a[i]
    print(total_height)

=======
Suggestion 10

def min_height_stools(people_heights):
    stool_heights = [0] * len(people_heights)
    stool_heights[0] = people_heights[0]
    for i in range(1, len(people_heights)):
        if people_heights[i] > stool_heights[i-1]:
            stool_heights[i] = stool_heights[i-1] + 1
        else:
            stool_heights[i] = people_heights[i]
    return sum(stool_heights) - sum(people_heights)
