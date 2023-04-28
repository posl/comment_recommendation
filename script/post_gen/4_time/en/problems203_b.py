Synthesizing 10/10 solutions

=======
Suggestion 1

def problem203_b():
    N,K = map(int, input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    print( (n * (n + 1) // 2) * 100 * k + (k * (k + 1) // 2) * n)

=======
Suggestion 3

def room_numbers(n, k):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += int(str(i) + "0" + str(j))
    return sum

=======
Suggestion 4

def sum_room(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum = sum + i*100 + j
    return sum

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    count = 0
    for i in range(n):
        for j in range(k):
            count += int(str(i+1) + '0' + str(j+1))
    print(count)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(N*100*K*(K+1)//2)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    print((n*100+k*10)**2)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    print((n+1)*n*k//2)

=======
Suggestion 9

def get_input():
    return list(map(int, input().split()))

=======
Suggestion 10

def get_input():
    return input()
