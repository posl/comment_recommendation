def getPermutations(s):
    if len(s) == 1:
        return [s]
    else:
        permutations = []
        for i in range(len(s)):
            permutations.extend([s[i] + p for p in getPermutations(s[:i] + s[i+1:])])
        return permutations
s = input()
print(len(set(getPermutations(s))))
The above code is the solution to the problem. The solution is pretty straightforward. We use recursion to get all the permutations of the string and then count the number of unique permutations.
The complexity of the solution is O(n!) where n is the length of the string.
The solution is available on GitHub.
Problem Statement
You are given a string S of length 3 consisting of lowercase English letters.
How many different strings can be obtained by permuting the characters in S?
Constraints
S is a string S of length 3 consisting of lowercase English letters.
Input
Input is given from Standard Input in the following format:
S
Output
Print the number of different strings that can be obtained by permuting the characters in S.
Sample Input 1
aba
Sample Output 1
3
By permuting the characters in S= aba, three different strings can be obtained: aab, aba, baa.
Sample Input 2
ccc
Sample Output 2
1
By permuting the characters in S= ccc, just one string can be obtained: ccc.
Sample Input 3
xyz
Sample Output 3
6
By permuting the characters in S= xyz, six different strings can be obtained: xyz, xzy, yxz, yzx, zxy, zyx.
Solution
The solution is available on GitHub.
The solution is pretty straightforward. We use recursion to get all the permutations of the string and then count the number of unique permutations.
The complexity of the solution is O(n!) where n is the length of the string.
The solution is available on GitHub.
Problem Statement
You are given a string S of length N consisting of lowercase English letters.
How many different strings can be obtained by permuting the characters in S?
Constraints
S is a string S of length N consisting of lowercase English letters.
1≤N≤8
Input
Input is given from Standard Input in the following format:
N
S
Output
Print the number of different strings that can be obtained by permut

if __name__ == '__main__':
    getPermutations()