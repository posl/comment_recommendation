def solve(n):
    if n <= 9:
        return n * (n + 1) // 2
    else:
        s = 0
        for i in range(1, 10):
            s += i * (n // 10 ** i)
        return s + solve(n % 10 ** (len(str(n)) - 1)) + 1
n = int(input())
print(solve(n) % 998244353)
This is a solution for the problem "A - 1, 2, 3, ...". The problem is here. The problem statement is as follows.
Given integers N and M, find the number of ways to choose N integers from 1, 2, ..., M that satisfy the following condition:
The sum of the chosen integers is a multiple of M.
Constraints
N, M are integers.
1 ≦ N ≦ M ≦ 10^9
Input
Input is given from Standard Input in the following format:
N M
Output
Print the answer as an integer.
Sample Input 1
2 5
Sample Output 1
2
There are two ways to choose two integers from 1, 2, 3, 4, 5 that satisfy the condition.
[1, 4]
[2, 3]
Sample Input 2
3 4
Sample Output 2
3
There are three ways to choose three integers from 1, 2, 3, 4 that satisfy the condition.
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
Sample Input 3
10 100000
Sample Output 3
0
There is no way to choose ten integers from 1, 2, 3, ..., 100000 that satisfy the condition.

if __name__ == '__main__':
    solve()