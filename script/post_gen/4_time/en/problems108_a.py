Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    if k % 2 == 0:
        print((k//2)**2)
    else:
        print((k//2)*(k//2+1))

=======
Suggestion 2

def main():
    k = int(input())

    if k % 2 == 0:
        print(int((k / 2)) ** 2)
    else:
        print(int(((k + 1) / 2) * (k / 2)))

=======
Suggestion 3

def main():
    k = int(input())
    print((k//2)*((k+1)//2))

=======
Suggestion 4

def main():
    K = int(input())
    print((K//2)*((K+1)//2))

=======
Suggestion 5

def num_of_ways_to_choose_a_pair(k):
    if k % 2 == 0:
        return (k//2)**2
    else:
        return ((k-1)//2)*((k+1)//2)

=======
Suggestion 6

def main():
    n = int(input())
    print(int((n/2) * ((n+1)/2)))

=======
Suggestion 7

def main():
    k = int(input())
    print(int(k/2 * (k-k/2)))

=======
Suggestion 8

def main():
    n = int(input())
    print(int(n / 2 * (n - n / 2)))

=======
Suggestion 9

def main():
    k = int(input())
    print((k//2)*((k-k//2)))
