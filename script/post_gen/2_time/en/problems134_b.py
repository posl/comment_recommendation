Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    if N % (2*D+1) == 0:
      print(N//(2*D+1))
    else:
      print(N//(2*D+1)+1)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + (2 * D)) // (2 * D + 1))

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    print((N-1)//(2*D+1) + 1)

=======
Suggestion 5

def read_ints():
    return list(map(int, input().split()))

N, D = read_ints()

=======
Suggestion 6

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 7

def main():
    # Write code here
    pass
