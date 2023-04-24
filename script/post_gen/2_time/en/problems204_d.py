Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) + max(T) // 2)

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int,input().split()))
    T.sort()
    ans = T[0]
    for i in range(1,N):
        ans += T[i]
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    T = [int(x) for x in input().split()]
    T.sort()
    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T))
    else:
        print(sum(T) - min(T))

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i]*(N-i)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(sum(t) - max(t) // 2)

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

=======
Suggestion 7

def main():
    N = int(input())
    T = [int(x) for x in input().split()]
    print(sum(T) - max(T) // 2)

=======
Suggestion 8

def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(sum(t)-max(t)+max(t)//2)

main()

=======
Suggestion 9

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    ans = 0
    ans += t[0]
    for i in range(1, n):
        ans += t[i]
    print(ans)

=======
Suggestion 10

def find_min_time(oven_list):
    oven_list.sort()
    if len(oven_list) == 1:
        return oven_list[0]
    elif len(oven_list) == 2:
        return oven_list[1]
    else:
        return oven_list[0] + find_min_time(oven_list[1:])
