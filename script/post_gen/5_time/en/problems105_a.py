Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    print(0 if n % k == 0 else 1)

=======
Suggestion 3

def main():
    # Take input here
    n,k = map(int,input().split())
    # Compute desired result here
    print(n%k)

main()
