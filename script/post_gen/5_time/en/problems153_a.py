Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, a = map(int, input().split())
    if h % a == 0:
        print(h // a)
    else:
        print(h // a + 1)

=======
Suggestion 2

def main():
    H,A = map(int,input().split())
    if H%A == 0:
        print(H//A)
    else:
        print(H//A + 1)

=======
Suggestion 3

def main():
    #input
    H, A = map(int, input().split())

    #compute

    #output
    if H % A == 0:
        print(H // A)
    else:
        print(H // A + 1)

=======
Suggestion 4

def main():
    h, a = map(int, input().split())
    print((h + a - 1) // a)

=======
Suggestion 5

def main():
    # input
    H, A = map(int, input().split())
    # compute
    count = H // A
    if H % A != 0:
        count += 1
    # output
    print(count)

=======
Suggestion 6

def f(h, a):
    return (h + a - 1) // a

h, a = map(int, input().split())
print(f(h, a))

=======
Suggestion 7

def main():
    H, A = map(int, input().split())
    print(-(-H // A))

=======
Suggestion 8

def main():
    h,a = input().split()
    print((int(h)-1)//int(a)+1)
