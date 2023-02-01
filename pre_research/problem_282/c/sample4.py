#Problem Statement
#You are given a string S of length N consisting of lowercase English letters, ,, and ". It is guaranteed that S contains an even number of ".
#Let 2K be the number of " in S. For each i=1,2,…,K, the characters from the (2i−1)-th " through the (2i)-th " are said to be enclosed.
#Your task is to replace each , in S that is not an enclosed character with . and print the resulting string.
#
#Constraints
#N is an integer between 1 and 2×10^5, inclusive.
#S is a string of length N consisting of lowercase English letters, ,, and ".
#S contains an even number of ".
#
#Input
#The input is given from Standard Input in the following format:
#N
#S
#
#Output
#Print the answer.
#
#Sample Input 1
#8
#"a,b"c,d
#
#Sample Output 1
#"a,b"c.d
#
#Sample Input 2
#5
#'''''
#
#Sample Output 2
#.....
#
#Sample Input 3
#20
#a,"t,"c,"o,"d,"e,"r,
#
#Sample Output 3
#a."t,"c."o,"d."e,"r.

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if all([S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()