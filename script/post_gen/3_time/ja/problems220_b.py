Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    A, B = input().split()
    print(int(A, K) * int(B, K))

=======
Suggestion 2

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(str, input().split())
    A = int(A, K)
    B = int(B, K)
    print(A * B)

=======
Suggestion 4

def main():
    k = int(input())
    a, b = map(str, input().split())
    print(int(a, k) * int(b, k))

=======
Suggestion 5

def main():
    K = int(input())
    A,B = map(int,input().split())
    print(int(str(A),K)*int(str(B),K))

=======
Suggestion 6

def main():
    K = int(input())
    A,B = map(int, input().split())
    #print(A,B)
    #print(K)
    A10 = 0
    B10 = 0
    for i in range(len(str(A))):
        A10 += int(str(A)[i]) * (K ** (len(str(A)) - i - 1))
    for j in range(len(str(B))):
        B10 += int(str(B)[j]) * (K ** (len(str(B)) - j - 1))
    print(A10 * B10)
