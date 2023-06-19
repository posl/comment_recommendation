def main():
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2)]
    print(a[r-1][c-1])
main()
In the above code, I used the following techniques:
1. Input
The first line of the input consists of two integers R and C. The second and third lines consist of two integers each, and they represent the matrix A.
2. Output
Print the answer as an integer.
3. Variables
In this problem, I used the following variables:
r: The row number of the matrix A.
c: The column number of the matrix A.
a: The matrix A.
4. Input and Output
The input is given from Standard Input in the following format:
R C
A_{1,1} A_{1,2}
A_{2,1} A_{2,2}
The output is given from Standard Output in the following format:
A_{R,C}
5. Functions
I used the following functions:
map: This function applies a function to each item of an iterable and returns a list of the results.
list: This function returns a list.
6. Iterations
I used the following iterations:
for _ in range(2): This line iterates 2 times.
7. List Comprehension
I used the following list comprehension:
a = [list(map(int, input().split())) for _ in range(2)]
This line creates a list of lists. The first list is the list of the two rows of the matrix A. The second list is the list of the two columns of the matrix A.
8. Indexing
I used the following indexing:
a[r-1][c-1]
This line returns the value at the intersection of the r-th row and the c-th column of the matrix A.
9. Print
I used the following print statement:
print(a[r-1][c-1])
This line prints the value at the intersection of the r-th row and the c-th column of the matrix A.
10. Main Function
I used the following main function:
