Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))

=======
Suggestion 2

def main():
    N = int(input())
    votes = {}
    for i in range(N):
        name = input()
        if name in votes:
            votes[name] += 1
        else:
            votes[name] = 1
    max_votes = max(votes.values())
    for name, num_votes in votes.items():
        if num_votes == max_votes:
            print(name)
            break

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_v = max(d.values())
    for k, v in d.items():
        if v == max_v:
            print(k)
            break

=======
Suggestion 4

def main():
    n = int(input())
    snuke = 0
    takahashi = 0
    aoki = 0
    for i in range(n):
        name = input()
        if name == 'snuke':
            snuke += 1
        elif name == 'takahashi':
            takahashi += 1
        elif name == 'aoki':
            aoki += 1
    if snuke >= takahashi and snuke >= aoki:
        print('snuke')
    elif takahashi >= snuke and takahashi >= aoki:
        print('takahashi')
    elif aoki >= snuke and aoki >= takahashi:
        print('aoki')

=======
Suggestion 5

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    d = {}
    for name in names:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
    print(max(d, key=d.get))

=======
Suggestion 6

def main():
    from collections import Counter
    n = int(input())
    c = Counter()
    for i in range(n):
        c[input()] += 1
    print(c.most_common()[0][0])

=======
Suggestion 7

def main():
    N = int(input())
    candidates = []
    for i in range(N):
        candidates.append(input())
    print(max(set(candidates), key=candidates.count))

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a.sort()
    b = []
    for i in range(n):
        b.append(a.count(a[i]))
    c = max(b)
    d = b.index(c)
    print(a[d])

=======
Suggestion 9

def   main () : 
     #input 
     N   =   int ( input ()) 
     S   =   [] 
     for   i   in   range ( N ): 
         S . append ( input ()) 

     #solve 
     d   =   {} 
     for   s   in   S : 
         if   s   in   d : 
             d [ s ]   +=   1 
         else : 
             d [ s ]   =   1 

     max_votes   =   max ( d . values ()) 
     for   k ,   v   in   d . items (): 
         if   v   ==   max_votes : 
             print ( k )

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(max(s,key=s.count))
