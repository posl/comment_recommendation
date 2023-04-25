Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if (A - K) == (B - K):
        print(K)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if (A - K) == (B - K):
        print(K)
    else:
        print("IMPOSSIBLE")

main()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 1:
        print("IMPOSSIBLE")
    else:
        print((a + b) // 2)

=======
Suggestion 6

def solve(a, b):
    if a == b:
        return 'IMPOSSIBLE'
    return str((a + b) // 2)

a, b = map(int, input().split())
print(solve(a, b))

=======
Suggestion 7

def main():
    #input
    a,b = map(int,input().split())
    #output
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print("IMPOSSIBLE")
    #return
    return
