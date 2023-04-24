Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k=int(input())
    if k%2==0:
        print((k//2)*(k//2))
    else:
        print((k//2)*(k//2+1))

=======
Suggestion 2

def main():
    K = int(input())
    even = K // 2
    odd = K // 2 + K % 2
    print(even * odd)

=======
Suggestion 3

def main():
    N = int(input())
    if N % 2 == 0:
        print(int(N/2 * (N/2-1)))
    else:
        print(int(N/2 * (N/2+1)))

=======
Suggestion 4

def main():
    k = int(input())
    print(int(k/2) * int((k+1)/2))

main()

=======
Suggestion 5

def main():
    k = int(input())
    print((k//2)*(k//2 + k%2))

=======
Suggestion 6

def main():
    K = int(input())
    print(int(K/2)*(K-int(K/2)))

=======
Suggestion 7

def main():
    k = int(input())
    print((k//2)*(k//2+(k%2)))

=======
Suggestion 8

def main():
    k = int(input())
    print((k//2)*((k+1)//2))

=======
Suggestion 9

def main():
    k = int(input())
    print(int((k/2)*(k/2)))

=======
Suggestion 10

def main():
    k = int(input())
    print(k*(k//2) + (k+1)//2)
