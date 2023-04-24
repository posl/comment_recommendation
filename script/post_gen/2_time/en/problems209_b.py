Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans += A[i] - 1
    if ans <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i % 2 == 1:
            A[i] -= 1
    if sum(A) <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i % 2 == 0:
            X -= A[i]
        else:
            X -= A[i] - 1
    if X >= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 1:
            a[i] -= 1
    if sum(a) <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i % 2 == 1:
            X -= A[i] - 1
        else:
            X -= A[i]
    if X >= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 1:
            ans += a[i] - 1
        else:
            ans += a[i]
    if ans <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = [a[i] for i in range(0,n,2)]
    c = [a[i]-1 for i in range(1,n,2)]
    d = b+c
    if sum(d)<=x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    # Input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # Process
    for i in range(N):
        if i % 2 == 1:
            A[i] -= 1
    if sum(A) <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    #input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    #output
    print('Yes' if sum([A[i] - i % 2 for i in range(N)]) <= X else 'No')

=======
Suggestion 10

def main():
    # Step #1. Read input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Step #2. Solve the problem
    # Step #2.1. Initialize the variable
    total = 0
    
    # Step #2.2. Calculate the total price
    for i in range(N):
        if i % 2 == 0:
            total += A[i]
        else:
            total += A[i] - 1
    
    # Step #2.3. Output the result
    if total <= X:
        print('Yes')
    else:
        print('No')

main()

Problem Statement

Takahashi's shop sells N products. The usual price of the i-th product is A_i yen (Japanese currency). It has a bargain sale today, with a discount of 1 yen off the usual prices for the 2-nd, 4-th, and the subsequent even-indexed products. The 1-st, 3-rd, and the subsequent odd-indexed products are sold for their usual prices. You have X yen. Can you buy all the N products with this money?

Constraints

1 ≦ N ≦ 100

1 ≦ X ≦ 10000

1 ≦ A_i ≦ 100

All values in input are integers.

Input

Input is given from Standard Input in the following format:

N X
A_1 A_2 ... A_N

Output

If you can buy all the N products, print Yes; otherwise, print No.

Sample Input 1

2 3
1 3

Sample Output 1

Yes

You can buy the 1-st product for 1 yen and the 2-nd product for 2 yen, 1 yen off the usual price. You have just enough money, 3 yen, to buy both of them.

Sample Input 2

4 10
3 3 4 4

Sample Output 2

No

You can buy these four products for 3 yen, 2 yen, 4 yen, and 3 yen, respectively. You need 12 yen to buy all of them, and since you have only 10 yen, you cannot buy all of them.

Sample Input 3

8 30
3 1 4 1 5 9 2
