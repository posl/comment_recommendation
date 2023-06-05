Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a, b):
    return b, a

=======
Suggestion 2

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

=======
Suggestion 3

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    for i in range(q):
        x = int(input())
        a[i%n], a[(i+1)%n] = a[(i+1)%n], a[i%n]
    print(*a)

=======
Suggestion 5

def swap(x):
    if x == 0:
        return 0
    else:
        return 1

=======
Suggestion 6

def swap(i, balls):
    if i == len(balls) - 1:
        balls[i], balls[0] = balls[0], balls[i]
    else:
        balls[i], balls[i+1] = balls[i+1], balls[i]
    return balls

N, Q = list(map(int, input().split()))
balls = list(range(1, N+1))
for _ in range(Q):
    x = int(input())
    balls = swap(x-1, balls)

print(' '.join(map(str, balls)))

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    balls = [i+1 for i in range(n)]
    for i in range(q):
        x = int(input())
        if balls[x-1] == n:
            balls[x-1], balls[x-2] = balls[x-2], balls[x-1]
        else:
            balls[x-1], balls[x] = balls[x], balls[x-1]
    print(' '.join(map(str, balls)))
