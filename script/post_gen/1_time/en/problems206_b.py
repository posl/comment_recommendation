Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    total = 0
    for i in range(1, N+1):
        total += i
        if total >= N:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            print(i)
            break

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        sum = sum + i
        if sum >= N:
            print(i)
            break

main()

=======
Suggestion 4

def main():
    n = int(input())
    i = 1
    total = 0
    while total < n:
        total += i
        i += 1
    print(i - 1)

=======
Suggestion 5

def main():
    N = int(input())
    x = 0
    for i in range(N):
        x += i
        if x >= N:
            print(i)
            break

=======
Suggestion 6

def main():
    N = int(input())
    #N = 100128
    #N = 12
    #N = 1
    #N = 2
    #N = 3
    #N = 4
    #N = 5
    #N = 6
    #N = 7
    #N = 8
    #N = 9
    #N = 10
    #N = 11
    #N = 12
    #N = 13
    #N = 14
    #N = 15
    #N = 16
    #N = 17
    #N = 18
    #N = 19
    #N = 20
    #N = 21
    #N = 22
    #N = 23
    #N = 24
    #N = 25
    #N = 26
    #N = 27
    #N = 28
    #N = 29
    #N = 30
    #N = 31
    #N = 32
    #N = 33
    #N = 34
    #N = 35
    #N = 36
    #N = 37
    #N = 38
    #N = 39
    #N = 40
    #N = 41
    #N = 42
    #N = 43
    #N = 44
    #N = 45
    #N = 46
    #N = 47
    #N = 48
    #N = 49
    #N = 50
    #N = 51
    #N = 52
    #N = 53
    #N = 54
    #N = 55
    #N = 56
    #N = 57
    #N = 58
    #N = 59
    #N = 60
    #N = 61
    #N = 62
    #N = 63
    #N = 64
    #N = 65
    #N = 66
    #N = 67
    #N = 68

=======
Suggestion 7

def main():
    N = int(input())
    print(int((N * 2) ** 0.5 - 0.5))

=======
Suggestion 8

def main():
    N = int(input())
    print(int((N*2)**0.5))

=======
Suggestion 9

def get_days(N):
    return int((2*N)**0.5)
