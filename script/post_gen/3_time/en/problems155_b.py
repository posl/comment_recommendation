Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                continue
            else:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i]%2 == 0:
            if A[i]%3 == 0 or A[i]%5 == 0:
                continue
            else:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                print("DENIED")
                return
    print("APPROVED")

main()

The above code is a solution to the problem posted here.

The problem is not very difficult. The only thing to watch out for is the formatting of the output. The output should be in the form of a string. So, we need to enclose the output string in quotes.

The sample input and output are given below:

Sample Input 1

5
6 7 9 10 31

Sample Output 1

APPROVED

Sample Input 2

3
28 27 24

Sample Output 2

DENIED

The above code is a solution to the problem posted here.

The problem is not very difficult. The only thing to watch out for is the formatting of the output. The output should be in the form of a string. So, we need to enclose the output string in quotes.

The sample input and output are given below:

Sample Input 1

5
6 7 9 10 31

Sample Output 1

APPROVED

Sample Input 2

3
28 27 24

Sample Output 2

DENIED

The above code is a solution to the problem posted here.

The problem is not very difficult. The only thing to watch out for is the formatting of the output. The output should be in the form of a string. So, we need to enclose the output string in quotes.

The sample input and output are given below:

Sample Input 1

5
6 7 9 10 31

Sample Output 1

APPROVED

Sample Input 2

3
28 27 24

Sample Output 2

DENIED

The above code is a solution to the problem posted here.

The problem is not very difficult. The only thing to watch out for is the formatting of the output. The output should be in the form of a string. So, we need to enclose the output string in quotes.

The sample input and output are given below:

Sample Input 1

5
6

=======
Suggestion 8

def main():
    n = int(input())
    a = input().split()
    for i in range(n):
        if int(a[i]) % 2 == 0:
            if int(a[i]) % 3 == 0 or int(a[i]) % 5 == 0:
                pass
            else:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(N):
        if A[i] % 2 == 0:
            if (A[i] % 3 == 0) or (A[i] % 5 == 0):
                continue
            else:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 1:
            continue
        if i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")
    return
