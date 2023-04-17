Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)
    return

=======

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print(N - K)

=======

def main():
    n,k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        print(1)

=======

def main():
    N, K = map(int, input().split())
    print(N % K)

=======

def main():
    n, k = map(int, input().split())
    print(n % k)

=======

def main():
    #Get the input
    N, K = map(int, input().split())
    #Get the result
    result = 0
    #If the number of crackers is not divisible by the number of users
    if N % K != 0:
        #Get the result
        result = 1
    #Print the result
    print(result)
