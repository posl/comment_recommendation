Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    x = 0
    for i in range(3):
        x = a[x]
    print(x)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    b = 0
    for i in range(3):
        b = a[b]
    print(b)

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

main()

=======
Suggestion 4

def main():
    # input
    a = list(map(int, input().split()))
    # compute
    ans = a[0]
    for i in range(3):
        ans = a[ans]
    # output
    print(ans)

=======
Suggestion 5

def main():
    a = input().split()
    b = []
    for i in a:
        b.append(int(i))
    count = 0
    while True:
        if count == 3:
            print(b[0])
            break
        else:
            count += 1
            b[0] = b[b[0]]

=======
Suggestion 6

def main():
    # Get input here
    inputString = input()
    # Calculate result here
    result = 0
    for i in range(3):
        result = int(inputString[result])
    # Print output here
    print(result)

=======
Suggestion 7

def problem():
    a = map(int, raw_input().split())
    for i in range(3):
        a = [a[x] for x in a]
    print a[0]

problem()

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    print(a[3])

=======
Suggestion 9

def main():
    # input
    a = list(map(int, input().split()))
    # compute
    for i in range(3):
        a = a[a[0]]
        # output
    print(a)

=======
Suggestion 10

def main():
    # input
    #a = list(map(int, input().split()))
    a = [int(x) for x in input().split()]
    # compute
    # output
    print(a[3])
