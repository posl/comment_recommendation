Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    print(int(k/2)*int(k/2+1))

=======
Suggestion 2

def func1():
    k=int(input())
    print(int(k/2)*int(k/2+1))

=======
Suggestion 3

def solution():
    K = int(input())
    print((K//2)*((K+1)//2))

=======
Suggestion 4

def main():
    k = int(input())
    print(int(k/2 * ((k+1)/2)))

=======
Suggestion 5

def main():
    k = int(input())
    print(k*k*k//8)

=======
Suggestion 6

def problems108_a():
    K = int(input())
    print(int(K/2)*(K-int(K/2)))

=======
Suggestion 7

def main():
    k = int(input())
    if k < 2 or k > 100:
        return
    count = 0
    for i in range(1, k + 1, 2):
        for j in range(2, k + 1, 2):
            count += 1
    print(count)

main()

=======
Suggestion 8

def fun(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            for j in range(1,n+1):
                if j % 2 == 1:
                    count += 1
    return count

print(fun(3))
print(fun(6))
print(fun(11))
print(fun(50))

=======
Suggestion 9

def main():
    k = int(input())
    print((k//2)*((k+1)//2))
    return

=======
Suggestion 10

def count_even_odd_pairs(k):
    # k is an integer
    # return the number of ways to choose a pair of
    # even number and odd number from 1, 2, ..., k
    count = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            if i % 2 == 0 and j % 2 != 0:
                count += 1
    return count
