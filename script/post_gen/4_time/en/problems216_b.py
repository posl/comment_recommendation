Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if len(names) == len(set(names)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    if len(names) == len(set(names)):
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    people = []
    for i in range(n):
        people.append(input())
    if len(people) == len(set(people)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input()
        names.append(name)
    if len(set(names)) == len(names):
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def solve():
    n = int(input())
    names = set()
    for _ in range(n):
        s, t = input().split()
        if (s, t) in names:
            print('Yes')
            return
        else:
            names.add((s, t))
    print('No')

=======
Suggestion 6

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input())
    if len(set(names)) == N:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a = input().split()
        s.append(a[0])
        t.append(a[1])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def solve():
    N = int(input())
    for i in range(N):
        S, T = input().split()
        for j in range(i):
            if S == Ss[j] and T == Ts[j]:
                print("Yes")
                return
        Ss.append(S)
        Ts.append(T)
    print("No")

Ss = []
Ts = []
solve()

=======
Suggestion 9

def main():
    # input
    N = int(input())
    names = []
    for i in range(N):
        names.append(input())
    names.sort()
    # compute

    # output
    for i in range(1,N):
        if names[i] == names[i-1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 10

def main():
    # Get the number of people
    n = int(input())
    # Get the family and given names
    names = [input().split() for _ in range(n)]
    # Check if there are any duplicated names
    for i in range(n):
        for j in range(i+1, n):
            if names[i] == names[j]:
                print('Yes')
                return
    # If there are no duplicated names, print 'No'
    print('No')
    return
