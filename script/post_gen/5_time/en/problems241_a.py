Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    b = a[0]
    for i in range(3):
        b = a[b]
    print(b)

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    i = 0
    while True:
        if a[i] == 0:
            print(i)
            break
        i = a[i]

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(10):
        k = a[k]
    print(k)

=======
Suggestion 5

def main():
    # Get input here
    a = [int(x) for x in input().strip().split()]
    
    # Calculate result here
    result = 0
    for i in range(3):
        result = a[result]
    
    # Print result here
    print(result)

=======
Suggestion 6

def main():
    a = input()
    a = a.split()
    a = [int(i) for i in a]
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    print(a[1])

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    print(a[3])
