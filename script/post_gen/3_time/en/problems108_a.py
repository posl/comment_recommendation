Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 2 == 0:
        print(int((n/2) * (n/2)))
    else:
        print(int((n/2) * (n/2+1)))

=======
Suggestion 2

def count_pairs(k):
    if k % 2 == 0:
        return k // 2 * (k // 2)
    else:
        return k // 2 * (k // 2 + 1)

=======
Suggestion 3

def main():
    N = int(input())
    if N % 2 == 0:
        print((N//2)**2)
    else:
        print((N//2)*(N//2 + 1))

=======
Suggestion 4

def main():
    k = int(input())
    print(int(k / 2) * int((k / 2) + (k % 2)))

=======
Suggestion 5

def main():
    K = int(input())
    print(int(K/2)*(K-int(K/2)))

=======
Suggestion 6

def main():
    K = int(input())
    print(K//2*(K//2 + K%2))

main()

=======
Suggestion 7

def main():
    K = int(input())
    print(K*(K-1)//2)

=======
Suggestion 8

def main():
    k = int(input())

    print((k//2) * ((k+1)//2))

=======
Suggestion 9

def main():
    #write your code here
    k = int(input())
    print(k * (k // 2))
