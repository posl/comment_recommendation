Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = i + 1
        while x != -1:
            x = p[x - 1]
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        j = i
        while j != -2:
            j = p[j] - 1
            cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        j = i
        while j != -1:
            j = p[j] - 1
            cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        cnt = 0
        x = i + 1
        while x != -1:
            x = p[x - 1]
            cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = i + 1
        while x != -1:
            x = p[x - 1]
            ans += 1
        print(ans)
        ans = 0

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = i + 1
        while x != -1:
            x = P[x - 1]
            ans += 1
            if x == -1:
                break
    print(ans)

=======
Suggestion 7

def func():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        count = 1
        j = i
        while p[j-1] != 0:
            j = p[j-1]
            count += 1
        if count > ans:
            ans = count
    print(ans)

=======
Suggestion 8

def get_generation(p, generation):
    if p == 1:
        return generation
    else:
        return get_generation(p_list[p-2], generation+1)

N = int(input())
p_list = list(map(int, input().split()))
print(get_generation(p_list[-1], 1))

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = max(ans, dfs(i, P))
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans = max(ans, dfs(i, p))
    print(ans)
