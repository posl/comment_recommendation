Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    if k % 2 == 0:
        print((k // 2) ** 2)
    else:
        print((k // 2) * ((k // 2) + 1))

=======
Suggestion 2

def main():
    k = int(input())
    if k % 2 == 0:
        print((k//2)**2)
    else:
        print((k//2)*(k//2+1))

=======
Suggestion 3

def main():
    k = int(input())
    even = k // 2
    odd = k - even
    print(even * odd)

=======
Suggestion 4

def main():
    k = int(input())
    print((k//2)*((k+1)//2))

=======
Suggestion 5

def main():
    k = int(input())
    a = k // 2
    b = k - a
    print(a * b)

=======
Suggestion 6

def main():
    K = int(input())

    even = K // 2
    odd = K - even

    print(even * odd)

=======
Suggestion 7

def main():
    k = int(input())
    print(int(k/2)*int(k/2+1))

=======
Suggestion 8

def main():
    k = int(input())
    print(int((k+1)/2)*int(k/2))
main()
