Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print(N)

=======
Suggestion 2

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(2**(N-1))

=======
Suggestion 3

def main():
    N = int(input())
    print(N*(N-1)//2)

=======
Suggestion 4

def main():
    N = int(input())
    #N=1の時は0を出力
    if N == 1:
        print(0)
    #N=2の時は1を出力
    elif N == 2:
        print(1)
    else:
        #N=3以上の時は、N-1個のお菓子を分け合う方法の数に、
        #A君が一個取り、B君がN-2個取る方法の数を足す
        print(N-1 + main(N-1))

=======
Suggestion 5

def main():
    n = int(input())
    print(n*(n-1)//2)

=======
Suggestion 6

def main():
    N = int(input())
    print(int(N*(N-1)/2))

=======
Suggestion 7

def main():
    n = int(input())
    print(n // 2)

=======
Suggestion 8

def main():
    N = int(input())
    print(N//2)
