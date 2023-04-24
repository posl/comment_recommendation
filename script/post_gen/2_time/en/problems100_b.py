Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, N = map(int, input().split())
    if D == 0:
        print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 2

def main():
    D, N = map(int, input().split())
    if N == 100:
        print(101 * (100 ** D))
    else:
        print(N * (100 ** D))

=======
Suggestion 3

def main():
    d, n = map(int, input().split())
    if n == 100:
        n += 1
    print(n * 100 ** d)

main()

=======
Suggestion 4

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(100 ** D * N)

=======
Suggestion 5

def main():
    D, N = list(map(int, input().split()))
    if D == 0:
        print(N)
    elif D == 1:
        print(N*100)
    else:
        print(N*10000)

=======
Suggestion 6

def main():
    d,n=map(int,input().split())
    if n<100:
        print(n*(100**d))
    else:
        print((n+1)*(100**d))
main()

=======
Suggestion 7

def get100s(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    else:
        return n * 10000

=======
Suggestion 8

def main():
    d,n = map(int,input().split())
    if n == 100:
        n = 101
    print(100**d*n)

=======
Suggestion 9

def main():
    # read input
    D, N = map(int, input().split())

    # compute output
    if N == 100:
        N += 1

    output = N * 100**D

    # print output
    print(output)

main()

=======
Suggestion 10

def main():
  # Read the input
  D, N = map(int, input().split())

  # Calculate the result
  if N == 100:
    N = 101
  result = N * 100 ** D

  # Print the result
  print(result)

main()
