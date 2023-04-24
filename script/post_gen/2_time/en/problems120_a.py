Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if b // a < c:
        print(b // a)
    else:
        print(c)

main()

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(min(b // a, c))

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    print(min(B//A, C))

=======
Suggestion 4

def main():
    #get input
    A, B, C = map(int, input().split())
    #calculate answer
    answer = min(B // A, C)
    #print answer
    print(answer)

=======
Suggestion 5

def main():
    #read the input
    A, B, C = map(int, input().split())
    #calculate the number of times
    if A * C > B:
        print(B // A)
    else:
        print(C)

=======
Suggestion 6

def vending_machine(a,b,c):
    return min(b//a,c)
