Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)

=======
Suggestion 4

def main():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)
            break

main()

=======
Suggestion 5

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            return

=======
Suggestion 6

def main():
    numbers = [int(x) for x in input().split()]
    for i in range(len(numbers)):
        if numbers[i] == 0:
            print(i+1)
            break

=======
Suggestion 7

def main():
    x = [int(x) for x in input().split()]
    print(x.index(0) + 1)

=======
Suggestion 8

def main():
    x = input().split()
    for i in range(1,6):
        if x[i-1] == '0':
            print(i)
            break
