Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 3

def main():
    #N = int(input())
    #N = 6
    #A = [1, 4, 1, 2, 2, 1]
    #N = 1
    #A = [1]
    #N = 11
    #A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    #N = 1000
    #A = [1] * 1000
    #N = 1000
    #A = [i for i in range(1, 1001)]
    #N = 1000
    #A = [i for i in range(1, 1001)]
    #N = 1000
    #A = [i for i in range(1, 1001)]
    N = 1000
    A = [i for i in range(1, 1001)]
    print(len(set(A)))
