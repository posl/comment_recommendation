Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - n)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(N * max(a) - sum(a))

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = sum(a) - n
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = sum(a) - n
    print(ans)

=======
Suggestion 7

def f(m, a):
    return sum(m % i for i in a)

n = int(input())
a = list(map(int, input().split()))
print(max(f(m, a) for m in range(2, 2*max(a))))

I'm not sure if this is a good approach, but I think it's good enough to solve the problem. I'm not sure if it's possible to do better than this.

This is my first post to this site. I'm trying to solve problems from the 2013 ACM-ICPC Asia Regional Daejeon Online Contest, and I've been trying to solve this problem for a while. I've tried a couple of different approaches, but they all seem to fail. I'm not sure if it's because I'm missing something, or if it's just impossible to solve this problem in the time limit.

I'm trying to solve this problem in Python 3.6.1.

I'm trying to solve the following problem:

You are given N positive integers a_1, a_2, ..., a_N.
For a non-negative integer m, let f(m) = (m mod a_1) + (m mod a_2) + ... + (m mod a_N).
Here, X mod Y denotes the remainder of the division of X by Y.
Find the maximum value of f.

Constraints

All values in input are integers.
2 ≦ N ≦ 3000
2 ≦ a_i ≦ 10^5

Input

Input is given from Standard Input in the following format:

N
a_1 a_2 ... a_N

Output

Print the maximum value of f.

Sample Input 1

3
3 4 6

Sample Output 1

10
f(11) = (11 mod 3) + (11 mod 4) + (11 mod 6) = 10 is the maximum value of f.

Sample Input 2

5
7 46 11 20 11

Sample Output 2

90

Sample Input 3

7
994 518 941 851 647 2 581

Sample Output 3

4527

I've tried a couple of different approaches, but they all seem to fail. I'm not sure if it's because I'm missing something, or if it's just impossible to solve this problem in the time limit.

I'm trying

=======
Suggestion 8

def solve():
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = a[-1]
    for i in range(1,N):
        ans += a[-1-i]-1
    return ans

print(solve())

=======
Suggestion 9

def  main():
     import  sys
