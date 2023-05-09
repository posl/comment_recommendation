def main():
    S = input()
    print(sum(S[i] != S[-i-1] for i in range(len(S)//2)))
main()
Sample Input 1
redcoder
Sample Output 1
1
Sample Input 2
vvvvvv
Sample Output 2
0
Sample Input 3
abcdabc
Sample Output 3
2
