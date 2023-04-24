Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

=======
Suggestion 2

def main():
    a = [int(x) for x in input().split()]
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

=======
Suggestion 3

def main():
    a = list(map(int,input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    i = 0
    for j in range(3):
        i = a[i]
    print(i)

=======
Suggestion 5

def main():
    a = input().split()
    n = 0
    for i in range(3):
        n = int(a[n])
    print(n)

=======
Suggestion 6

def main():
    a = input().split()
    num = 0
    for i in range(3):
        num = int(a[num])
    print(num)

=======
Suggestion 7

def main():
    a = input().split()
    current = 0
    for i in range(3):
        current = int(a[current])
    print(current)

=======
Suggestion 8

def main():
    a = input().split()
    print(a[1])

=======
Suggestion 9

def main():
    #read input
    a = input()
    a = a.split()

    #convert the input to integers
    for i in range(len(a)):
        a[i] = int(a[i])

    #set the starting value of the screen
    screen = 0

    #loop through the input 3 times
    for j in range(3):
        #set the screen to the value of the input at that index
        screen = a[screen]

    #print the final value of the screen
    print(screen)
