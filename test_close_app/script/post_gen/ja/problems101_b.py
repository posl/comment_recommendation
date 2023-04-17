Synthesizing 10/10 solutions

=======

def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if int(N) % sum == 0:
        print("Yes")
    else:
        print("No")

=======

def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======

def main():
    N = int(input())
    sum = 0
    for i in str(N):
        sum += int(i)
    if N % sum == 0:
        print("Yes")
    else:
        print("No")

=======

def main():
    N = int(input())
    sum = 0
    for i in str(N):
        sum += int(i)
    if N % sum == 0:
        print("Yes")
    else:
        print("No")
main()

=======

def main():
    N = int(input())
    if N % sum(map(int, str(N))) == 0:
        print("Yes")
    else:
        print("No")

=======

def main():
    # input
    N = int(input())

    # compute
    S = 0
    for i in str(N):
        S += int(i)

    # output
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======

def main():
    N = int(input())
    print("Yes" if N % sum(list(map(int, list(str(N))))) == 0 else "No")

=======

def main():
    N = input()
    N = int(N)
    Nsum = 0
    for n in N:
        Nsum += int(n)
    if N % Nsum == 0:
        print("Yes")
    else:
        print("No")

=======

def sum_of_digits(n):
    return sum([int(i) for i in list(str(n))])

n = int(input())

=======

def sum_of_digits(n):
    return sum(int(i) for i in str(n))
