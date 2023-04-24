Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) // 2)

main()

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i] * (N - i)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) + max(T) // 2)

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))

    T.sort()
    ans = T[0]
    for i in range(1, N):
        ans += T[i]
    ans -= T[0] // 2

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T = [int(x) for x in input().split()]
    T.sort()
    print(sum(T)-T[-1]+T[-1]//2)

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    if N == 1:
        print(T[0])
        return
    if N == 2:
        print(T[0]+T[1])
        return
    if N == 3:
        print(T[0]+T[1])
        return
    if N == 4:
        print(T[0]+T[1]+T[2])
        return
    if N == 5:
        print(T[0]+T[1]+T[2]+T[3])
        return
    if N == 6:
        print(T[0]+T[1]+T[2]+T[3]+T[4])
        return
    if N == 7:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5])
        return
    if N == 8:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5]+T[6])
        return
    if N == 9:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5]+T[6]+T[7])
        return
    if N == 10:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5]+T[6]+T[7]+T[8])
        return
    if N == 11:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5]+T[6]+T[7]+T[8]+T[9])
        return
    if N == 12:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5]+T[6]+T[7]+T[8]+T[9]+T[10])
        return
    if N == 13:
        print(T[0]+T[1]+T[2]+T[3]+T[4]+T[5]+T[6]+T[7]+T[8]+T[9]+T[10]+T[11])

=======
Suggestion 7

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T = T[::-1]
    ans = T[0]
    for i in range(1, N):
        ans += T[i]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[0] + sum(t[1:]) - t[0] // 2)

=======
Suggestion 9

def min_time():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i] * (N - i)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

main()

I think this problem is a bit tricky. The idea is to use the two ovens as follows to cook all the dishes in 13 minutes. The first oven: Cook Dishes 5 and 1 in this order. The second oven: Cook Dishes 2, 4, and 3 in this order. The first oven is used for 5 + 1 = 6 minutes. The second oven is used for 2 + 4 + 3 = 9 minutes. The total time is 6 + 9 = 15 minutes. However, we can use the first oven for 5 + 1 + 3 = 9 minutes instead. Then, the second oven is used for 2 + 4 = 6 minutes. The total time is 9 + 6 = 15 minutes. We can reduce the total time from 15 minutes to 13 minutes by using the first oven for 3 minutes longer than the second oven.
