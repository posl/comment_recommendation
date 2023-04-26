Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (i//A + j//B) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(N):
            for k in range(B):
                for l in range(N):
                    if (i + j + k + l) % 2 == 0:
                        print(".", end="")
                    else:
                        print("#", end="")
            print()
    return

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    for i in range(A*N):
        for j in range(B*N):
            if ((i//A) + (j//B)) % 2 == 0:
                print(".", end="")
            else:
                print("#", end="")
        print()

=======
Suggestion 4

def main():
    N,A,B = map(int,input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (i//A + j//B)%2 == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            if i % 2 == 0:
                print('#' * B + '.' * B, end='')
            else:
                print('.' * B + '#' * B, end='')
        print()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            if i % 2 == 0:
                print("#"*B, end="")
            else:
                print("."*B, end="")
        print()
    for i in range(N):
        for j in range(A):
            if i % 2 == 0:
                print("."*B, end="")
            else:
                print("#"*B, end="")
        print()

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    for i in range(A):
        for j in range(N):
            for k in range(B):
                for l in range(N):
                    if (i+j+k+l)%2 == 0:
                        print(".", end="")
                    else:
                        print("#", end="")
            print()

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    ans = []
    for i in range(A*N):
        ans.append([])
        for j in range(B*N):
            ans[i].append('.')
    for i in range(N):
        for j in range(N):
            if (i+j)%2 == 0:
                for k in range(A):
                    for l in range(B):
                        ans[A*i+k][B*j+l] = '#'
    for i in range(A*N):
        print(''.join(ans[i]))

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    ans = []
    for i in range(A*N):
        ans.append([])
        for j in range(B*N):
            if (i//A+j//B)%2 == 0:
                ans[i].append('.')
            else:
                ans[i].append('#')
    for i in range(A*N):
        print(''.join(ans[i]))

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    w = ["." for i in range(A * N)]
    b = ["#" for i in range(A * N)]
    for i in range(B * N):
        if i % 2 == 0:
            for j in range(A * N):
                print(w[j], end="")
            print()
        else:
            for j in range(A * N):
                print(b[j], end="")
            print()
