Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,d = map(int,input().split())
    if n%(2*d+1)==0:
        print(n//(2*d+1))
    else:
        print(n//(2*d+1)+1)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 3

def main():
    N,D = input().split()
    N = int(N)
    D = int(D)
    if N % (2 * D + 1) == 0:
        print(N // (2 * D + 1))
    else:
        print(N // (2 * D + 1) + 1)

=======
Suggestion 4

def main():
    n,d = map(int,input().split())
    print(n//(d*2+1)+1 if n%(d*2+1)!=0 else n//(d*2+1))

=======
Suggestion 5

def check_apple_tree(N, D):
    if N % (2*D + 1) == 0:
        return N // (2*D + 1)
    else:
        return N // (2*D + 1) + 1

=======
Suggestion 6

def count_apple_trees(N, D):
    if N <= D:
        return 1
    else:
        return 2

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    print(int((n + 2 * d) / (2 * d + 1)))

=======
Suggestion 8

def get_input():
    n, d = map(int, input().split())
    return n, d

=======
Suggestion 9

def main():
    n,d = map(int,input().split())
    print((n+2*d)//(2*d+1))
