Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(min(A), max(B) + 1):
        if min(A) <= i <= max(B):
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        if all([A[j] <= i and i <= B[j] for j in range(N)]):
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        if all([A[j] <= i <= B[j] for j in range(N)]):
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(min(B)-max(A)+1 if min(B)-max(A)+1 > 0 else 0)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for x in range(1, 1001):
        if all(A[i] <= x <= B[i] for i in range(N)):
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        count += B[i] - A[i] + 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    A = input().split()
    B = input().split()
    for i in range(N):
        A[i] = int(A[i])
        B[i] = int(B[i])
    count = 0
    for x in range(1,1001):
        flag = True
        for i in range(N):
            if A[i] > x or B[i] < x:
                flag = False
                break
        if flag == True:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(B)
    count = 0
    for i in range(1, 1001):
        for j in range(N):
            if i < A[j] or i > B[j]:
                break
            elif j == N-1:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = ans + (B[i] - A[i] + 1)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    x = list(range(min(A), max(B) + 1))
    count = 0
    for i in x:
        if all([i >= A[j] and i <= B[j] for j in range(N)]):
            count += 1
    print(count)
