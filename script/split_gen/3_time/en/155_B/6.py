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
