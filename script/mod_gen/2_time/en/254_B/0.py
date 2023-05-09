def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        return [1] + [pascal(n-1)[i] + pascal(n-1)[i+1] for i in range(len(pascal(n-1))-1)] + [1]
N = int(input())
for i in range(N):
    print(*pascal(i))
I don't know if this is the best way to solve this, but I tried to implement the Pascal's triangle.
I used the recursive function to get the Pascal's triangle.
The first line is 1, so I set the initial value of n to 0.
The second line is 1 1, so I set the initial value of n to 1.
The third line is 1 2 1, so I set the initial value of n to 2.
The fourth line is 1 3 3 1, so I set the initial value of n to 3.
The fifth line is 1 4 6 4 1, so I set the initial value of n to 4.
The sixth line is 1 5 10 10 5 1, so I set the initial value of n to 5.
The seventh line is 1 6 15 20 15 6 1, so I set the initial value of n to 6.
The eighth line is 1 7 21 35 35 21 7 1, so I set the initial value of n to 7.
The ninth line is 1 8 28 56 70 56 28 8 1, so I set the initial value of n to 8.
The tenth line is 1 9 36 84 126 126 84 36 9 1, so I set the initial value of n to 9.
I used the for loop to output each line.
I used the * operator to print the list with a space between each element.
I used the * operator to print the list with a space between each element.
This is the first time I've seen this operator. I've never seen it in any of the books I've read. It's really useful!
I've read the book "Python Cookbook" and it's really useful. I think

if __name__ == '__main__':
    pascal()