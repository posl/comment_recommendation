Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
            print()
main()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print(end='')
            print()
        print()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
main()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    for i in range(0, N):
        for j in range(0, A):
            for k in range(0, N):
                for l in range(0, B):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2 == 0:
                        print(".", end="")
                    else:
                        print("#", end="")
                print()
        print()

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    print('.' if (i+j)%2 == 0 else '#', end='')
                print(end='')
            print()
        print()

=======
Suggestion 9

def main():
    N,A,B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+j)%2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print(end='')
            print()
        print()
