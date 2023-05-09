def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if A <= i <= A + B - 1 and B <= j <= B + A - 1 or A <= i <= A + B - 1 and B - A + 1 <= j <= B or A - B + 1 <= i <= A and B <= j <= B + A - 1 or A - B + 1 <= i <= A and B - A + 1 <= j <= B:
                print('#', end='')
            else:
                print('.', end='')
        print()
main()
This is a problem that I solved in the past, but I didn’t have time to write about it. It is a problem that requires a lot of mathematical knowledge, so I am not sure if it is appropriate to write about it in this blog. I will write about it anyway.
Problem Statement
Given a string S of length N, find the number of pairs of indices (i,j) such that 1≦ i≦ j≦ N and the substring Si…Sj is a palindrome.
Constraints
1≦ N≦ 10^5
S consists of lowercase English letters
Input
Input is given from Standard Input in the following format:
N
S
Output
Print a single integer, the number of pairs of indices (i,j) such that 1≦ i≦ j≦ N and the substring Si…Sj is a palindrome.
Sample Input 1
2
aa
Sample Output 1
3
The three pairs are (1,1), (1,2), (2,2).
Sample Input 2
3
aba
Sample Output 2
4
The four pairs are (1,1), (1,2), (2,3), (3,3).
Sample Input 3
4
abba
Sample Output 3
6
The six pairs are (1,1), (1,2), (1,4), (2,2), (2,4), (4,4).
Sample Input 4
8
tactcoa
Sample Output 4
29
The 29 pairs are (1,

if __name__ == '__main__':
    main()