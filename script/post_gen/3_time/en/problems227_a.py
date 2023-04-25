Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, A = map(int, input().split())
    ans = (A + K - 1) % N
    if ans == 0:
        ans = N
    print(ans)

=======
Suggestion 2

def main():
    n, k, a = (int(x) for x in input().split())
    print((a + k - 2) % n + 1)

main()

=======
Suggestion 3

def main():
    N, K, A = map(int, input().split())
    print((A+K-2)%N+1)

=======
Suggestion 4

def main():
    n,k,a = [int(x) for x in input().split()]
    print((a+k-2)%n+1)

=======
Suggestion 5

def main():
    n,k,a = map(int,input().split())
    print((a+k-2)%n+1)

=======
Suggestion 6

def solve(n, k, a):
    return (a + k - 2) % n + 1

=======
Suggestion 7

def get_last_card(N, K, A):
    if N == 1:
        return 1
    if K < N:
        return (A + K - 1) % N + 1
    else:
        return (A + K - 1) % N

=======
Suggestion 8

def get_last_person(N, K, A):
    return (A + K - 1) % N

=======
Suggestion 9

def main():
    #write your code here
    pass
