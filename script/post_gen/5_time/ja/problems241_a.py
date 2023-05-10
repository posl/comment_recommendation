Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = [int(x) for x in input().split()]
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

main()

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a = a[a[0]]
    print(a)

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    #print(a)
    count = 0
    while True:
        if a[count] == 0:
            break
        count = a[count]
    print(count)

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

=======
Suggestion 7

def answer(a):
    result = 0
    for i in range(3):
        result = a[result]
    return result

=======
Suggestion 8

def solve():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 9

def main():
    a = list(map(int, input().split()))
    num = 0
    for i in range(3):
        num = a[num]
    print(num)
