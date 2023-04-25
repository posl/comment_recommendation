Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    print(sum(P[:K]))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    price = list(map(int, input().split()))
    price.sort()
    print(sum(price[:K]))

=======
Suggestion 5

def main():
    # input
    N, K = map(int, input().split())
    Ps = list(map(int, input().split()))
    # compute
    Ps.sort()
    ans = sum(Ps[:K])
    # output
    print(ans)

=======
Suggestion 6

def main():
    # Read a line
    line = input()
    # Split the line into a list of strings
    line = line.split()
    # Convert the list of strings into a list of integers
    line = [int(x) for x in line]
    # Read another line
    line2 = input()
    # Split the line into a list of strings
    line2 = line2.split()
    # Convert the list of strings into a list of integers
    line2 = [int(x) for x in line2]
    # Sort the list
    line2.sort()
    # Add the first K elements of the list
    print(sum(line2[:line[1]]))
