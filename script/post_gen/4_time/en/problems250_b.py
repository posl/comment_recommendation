Synthesizing 10/10 solutions

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
                print()
        print()

main()

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if ((i + k) % 2 == 0):
                        print('#', end='')
                    else:
                        print('.', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 3

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0:
                        print('.',end='')
                    else:
                        print('#',end='')
                print()
        print()

=======
Suggestion 4

def main():
    n,a,b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 5

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2==0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("",end="")
            print("")
        print("")

=======
Suggestion 6

def main():
    N,A,B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+j)%2==0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("",end="")
            print("")
        print("")

=======
Suggestion 7

def solve():
  n,a,b = map(int,input().split())
  for i in range(n):
    for j in range(a):
      for k in range(n):
        for l in range(b):
          if i%2 == 0:
            if k%2 == 0:
              print(".",end="")
            else:
              print("#",end="")
          else:
            if k%2 == 0:
              print("#",end="")
            else:
              print(".",end="")
        print("")
solve()

=======
Suggestion 8

def printTile(N,A,B):
    for i in range(0,N):
        for j in range(0,A):
            for k in range(0,N):
                for l in range(0,B):
                    if (i+k)%2==0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
    return

=======
Suggestion 9

def print_tiles(N, A, B):
    for i in range(0, N):
        for j in range(0, A):
            for k in range(0, N):
                if (i + j) % 2 == 0:
                    for l in range(0, B):
                        if (k + l) % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                else:
                    for l in range(0, B):
                        if (k + l) % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
            print('')
    return

N, A, B = map(int, input().split())
print_tiles(N, A, B)

=======
Suggestion 10

def main():
    # Get input here
    n, a, b = map(int, input().strip().split())
    # Calculate result here
    result = solve(n, a, b)
    # Output result here
    for line in result:
        print(line)
