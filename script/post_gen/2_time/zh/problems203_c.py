Synthesizing 10/10 solutions

=======
Suggestion 1

def get_sum(n, k):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += i*100 + j
    return sum

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    print(sum([100 * n + k for n in range(1, N + 1) for k in range(1, K + 1)]))

=======
Suggestion 3

def get_sum(N, K):
    return sum([int(str(i) + str(j) + str(k)) for i in range(1, N + 1) for j in range(1, K + 1) for k in range(1, K + 1)])

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += 100*i+j
    print(sum)

main()

=======
Suggestion 5

def problems203_b():
    n,k = map(int,input().split())
    print((n*(n+1)*k*100)//2)
problems203_b()

=======
Suggestion 6

def main():
    print('start')
    n, k = map(int, input().split())
    print('n = ', n)
    print('k = ', k)
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += i*100 + j
    print(sum)
    print('end')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    print(sum([int(str(i) + str(j)) for i in range(1, N + 1) for j in range(1, K + 1)]))

=======
Suggestion 8

def room_number_sum(n, k):
    room_sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            room_sum += int(str(i) + '0' + str(j))
    return room_sum

=======
Suggestion 9

def sum_of_rooms(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            room = i*100+j
            sum += room
    return sum

=======
Suggestion 10

def main():
    N,K = input().split()
    N = int(N)
    K = int(K)
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += i*100 + j
    print(sum)
