Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, A = map(int, input().split())
    print((A + K - 2) % N + 1)

=======
Suggestion 2

def main():
    n, k, a = map(int, input().split())
    print((a + k - 2) % n + 1)

=======
Suggestion 3

def main():
    N, K, A = map(int, raw_input().split())
    print (A + K - 1) % N + 1

main()

=======
Suggestion 4

def main():
    N, K, A = [int(x) for x in raw_input().split()]
    print (A + K - 1) % N + 1

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    a -= 1
    print((a + k) % n + 1)

=======
Suggestion 6

def get_last_person(N, K, A):
    last_person = A + K - 1
    while last_person > N:
        last_person -= N
    return last_person

N, K, A = map(int, input().split())
print(get_last_person(N, K, A))

=======
Suggestion 7

def getPerson(N, K, A):
    person = (A + K - 1) % N
    if person == 0:
        person = N
    return person

=======
Suggestion 8

def main():
    N, K, A = map(int, input().split())
    print((A + K - 1) % N + 1)
main()

import sys
input = sys.stdin.readline

=======
Suggestion 9

def last_person(n, k, a):
    return (a + k - 2) % n + 1
