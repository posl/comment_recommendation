Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_room_number(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100 + j
    return sum

=======
Suggestion 2

def sum_room(n, k):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += i*100 + j
    return sum

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    print(100*n*(n+1)//2*k)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    total = 0
    for i in range(n):
        for j in range(1, k + 1):
            total += int(str(i + 1) + '0' + str(j))
    print(total)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    result = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            result += i*100+j
    print(result)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    print(((n*(n+1))//2)*100*k + (k*(k+1)//2)*n)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    sum = 0
    for i in range(n):
        for j in range(k):
            sum += (i + 1) * 100 + (j + 1)
    print(sum)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    result = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            result += i*100 + j
    print(result)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    print(n * (n + 1) * k * 100 // 2)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    result = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            result += 100 * i + j
    print(result)
