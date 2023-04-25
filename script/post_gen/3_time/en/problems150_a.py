Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K, X = map(int, input().split())
    if K * 500 >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    k, x = map(int, input().split())
    if k * 500 >= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    K, X = map(int, input().split())
    if 500 * K >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    k, x = map(int, input().split())
    if k * 500 >= x:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 5

def main():
    K, X = input().split()
    K = int(K)
    X = int(X)
    if K * 500 >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    K, X = [int(i) for i in input().split()]
    if 500*K >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    # Read the input
    K, X = map(int, input().split())

    # Check if the coins add up to X yen or more
    if K * 500 >= X:
        print("Yes")
    else:
        print("No")
