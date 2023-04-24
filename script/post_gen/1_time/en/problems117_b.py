Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[-1] < sum(L[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[-1] < sum(L[:-1]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort(reverse=True)
    print('Yes' if L[0] < sum(L[1:]) else 'No')

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    maxL = L.pop()
    if maxL < sum(L):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def polygon(N, L):
    L.sort()
    if L[-1] < sum(L[:-1]):
        return "Yes"
    else:
        return "No"

=======
Suggestion 9

def polygon(n, l):
    #print(n, l)
    l.sort()
    #print(l)
    if l[-1] < sum(l[:-1]):
        return "Yes"
    else:
        return "No"
