Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a = [a[a[i]] for i in range(10)]
    print(a[0])

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a = [a[a[0]]] + a[1:]
    print(a[0])

=======
Suggestion 4

def main():
    a = [int(i) for i in input().split()]
    for i in range(3):
        a = [a[j] for j in range(10) if j != a[j]]
    print(a[0])

=======
Suggestion 5

def main():
    a = map(int, raw_input().split())
    n = 0
    for i in range(3):
        n = a[n]
    print n

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    print(a[1])

=======
Suggestion 7

def main():
    # Get input here
    a = list(map(int, input().strip().split()))
    # Calculate result here
    a = a[1:] + [a[0]]
    a = a[1:] + [a[0]]
    a = a[1:] + [a[0]]
    # Print output here
    print(a[0])

=======
Suggestion 8

def main():
    # get input
    a = list(map(int, input().split()))
    # set initial value
    k = 0
    # set counter
    count = 0
    # loop until counter reaches 3
    while count < 3:
        # set next value
        k = a[k]
        # increment counter
        count += 1
    # print result
    print(k)
