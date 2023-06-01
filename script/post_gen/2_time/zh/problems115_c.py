Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    sum = 0
    for i in range(n):
        if i == n-1:
            sum += p[i]/2
        else:
            sum += p[i]
    print(int(sum))

=======
Suggestion 2

def main():
    n = int(input())
    p = []
    for i in range(0,n):
        p.append(int(input()))
    p.sort()
    p[n-1] = int(p[n-1]/2)
    print(sum(p))

=======
Suggestion 3

def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort()
    prices[-1] = prices[-1] / 2
    print(int(sum(prices)))

=======
Suggestion 4

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))

    p.sort()
    p.reverse()

    total = 0
    for i in range(n):
        if i == 0:
            total += p[i] / 2
        else:
            total += p[i]

    print(int(total))

=======
Suggestion 5

def main():
    #import time
    #start = time.clock()
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))
    #end = time.clock()
    #print(end - start)

=======
Suggestion 6

def get_input():
    N = int(input())
    p = [int(input()) for i in range(N)]
    return N, p

=======
Suggestion 7

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 8

def problems115_b():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    print(p[0]//2 + sum(p[1:]))

=======
Suggestion 9

def main():
    n = int(raw_input())
    plist = []
    for i in xrange(n):
        plist.append(int(raw_input()))
    plist.sort(reverse=True)
    plist[0] = plist[0] / 2
    print sum(plist)
