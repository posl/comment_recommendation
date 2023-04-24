Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1, 2):
        if len(divisors(i)) == 8:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            if len(factors(i)) == 8:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i%2 == 1:
            if len([j for j in range(1,i+1) if i%j == 0]) == 8:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i % 2 == 0:
            continue
        if len([j for j in range(1,i+1) if i % j == 0]) == 8:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i%2==1:
            if len([x for x in range(1,i+1) if i%x==0])==8:
                count+=1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1,2):
        if i%2 == 1:
            if count_divisors(i) == 8:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    if N % 2 == 0:
        N -= 1
    cnt = 0
    for i in range(1, N+1, 2):
        if count_divisor(i) == 8:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    count = 0

    for i in range(1, N+1, 2):
        if i == 1:
            continue
        if len(list(divisor(i))) == 8:
            count += 1

    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    #約数の個数を数える
    count = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            count[j] += 1
    #奇数かつ約数が8個の数を数える
    ans = 0
    for i in range(1, N+1, 2):
        if count[i] == 8:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    print(solve(N))
