Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        ans = max(ans, int(N[:i]) * int(N[i:]))
    print(ans)

=======
Suggestion 2

def main():
    N = input()
    max = 0
    for i in range(1, len(N)):
        a = int(N[:i])
        b = int(N[i:])
        if a * b > max:
            max = a * b
    print(max)

=======
Suggestion 3

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    if len(N) == 2:
        print(N[0] * N[1])
    else:
        N.sort(reverse=True)
        print(N[0] * N[1])

=======
Suggestion 4

def main():
    N = input()
    lenN = len(N)
    if lenN == 2:
        print(int(N))
        return
    if lenN == 3:
        print(max(int(N[0]) * int(N[1:]), int(N[:2]) * int(N[2:])))
        return
    if lenN == 4:
        print(max(int(N[0]) * int(N[1:]) , int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:])))
        return
    if lenN == 5:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:])))
        return
    if lenN == 6:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:]), int(N[0:5]) * int(N[5:])))
        return
    if lenN == 7:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:]), int(N[0:5]) * int(N[5:]), int(N[0:6]) * int(N[6:])))
        return
    if lenN == 8:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:]), int(N[0:5]) * int(N[5:]), int(N[0:6]) * int(N[6:]), int(N[0:7]) * int(N[7:])))
        return
    if lenN == 9:
        print(max(int(N[0]) * int(N[1:

=======
Suggestion 5

def main():
    n = input()
    n = [int(i) for i in n]
    n.sort(reverse=True)
    a = n[0]
    b = 0
    for i in n[1:]:
        b = b*10 + i
    print(a*b)

=======
Suggestion 6

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort(reverse=True)
    print(N[0] * N[1])

=======
Suggestion 7

def main():
    N = input()
    N = int(N)
    N = str(N)
    ans = 0
    for i in range(1,len(N)):
        ans = max(ans, int(N[:i]) * int(N[i:]))
    print(ans)

=======
Suggestion 8

def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    print(int("".join(N[0:2])) * int("".join(N[2:4])))

=======
Suggestion 9

def main():
    N = input()
    N = list(map(int, N))
    N.sort(reverse = True)
    N = list(map(str, N))
    N = ''.join(N)
    N = int(N)
    N = str(N)
    N = list(N)
    N = list(map(int, N))
    print(N[0] * N[1])
