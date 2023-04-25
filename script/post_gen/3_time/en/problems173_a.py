Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

=======
Suggestion 2

def main():
    N = int(input())
    print(N%1000)
    if N%1000 == 0:
        print(0)
    else:
        print(1000 - N%1000)

=======
Suggestion 3

def main():
    N = int(input())
    print(N % 1000 if N % 1000 != 0 else 1000)

=======
Suggestion 4

def main():
    N = int(input())
    print(1000 - N%1000 if N%1000 != 0 else 0)

main()

=======
Suggestion 5

def main():
    N = int(input())
    print(1000 - (N % 1000))

=======
Suggestion 6

def main():
    #input
    N = int(input())

    #calculate
    ans = 1000 - N % 1000
    if ans == 1000:
        ans = 0

    #output
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    print(N%1000)

=======
Suggestion 8

def main():
    N = int(input())
    print(N % 1000)
    return

main()

=======
Suggestion 9

def main():
    #Read input
    N = int(input())
    #Calculate change
    change = N % 1000
    #Output result
    if change == 0:
        print(0)
    else:
        print(1000 - change)
