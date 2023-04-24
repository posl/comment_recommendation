Synthesizing 10/10 solutions

=======
Suggestion 1

def pascal(n):
    if n == 0:
        return [1]
    else:
        return [1] + [pascal(n-1)[i] + pascal(n-1)[i+1] for i in range(len(pascal(n-1))-1)] + [1]

n = int(input())
for i in range(n):
    print(*pascal(i))

=======
Suggestion 2

def main():
    n = int(input())
    a = [[1]]
    for i in range(n-1):
        a.append([1])
        for j in range(i):
            a[i+1].append(a[i][j]+a[i][j+1])
        a[i+1].append(1)
    for i in range(n):
        print(*a[i])

=======
Suggestion 3

def pascal_triangle(n):
    if n == 0:
        return [1]
    else:
        return [1] + [pascal_triangle(n-1)[i] + pascal_triangle(n-1)[i+1] for i in range(n-1)] + [1]

N = int(input())
for i in range(N):
    print(*pascal_triangle(i))

=======
Suggestion 4

def pascal(n):
    if n == 0:
        return [1]
    else:
        p = pascal(n-1)
        return [1] + [p[i] + p[i+1] for i in range(n-1)] + [1]

N = int(input())
for i in range(N):
    print(*pascal(i))

=======
Suggestion 5

def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        a = pascal(n-1)
        b = [1]
        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        b.append(1)
        return b

=======
Suggestion 6

def pascal(n):
	if n == 0:
		return [1]
	else:
		return [1] + [pascal(n-1)[i-1] + pascal(n-1)[i] for i in range(1,n)] + [1]

=======
Suggestion 7

def pascal_triangle(row):
    if row==0:
        return [1]
    elif row==1:
        return [1,1]
    else:
        prev_row=pascal_triangle(row-1)
        new_row=[1]
        for i in range(len(prev_row)-1):
            new_row.append(prev_row[i]+prev_row[i+1])
        new_row.append(1)
        return new_row

=======
Suggestion 8

def print_pascal(n):
    if n == 1:
        print(1)
    else:
        print_pascal(n - 1)
        for i in range(n):
            if i == 0 or i == n - 1:
                print(1, end=' ')
            else:
                print(1, end=' ')
                for j in range(1, i):
                    print(1, end=' ')
                print(1, end=' ')
        print()

=======
Suggestion 9

def pascal_triangle(n): # n is number of rows
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

n = int(input())
for row in pascal_triangle(n):
    print(*row)

=======
Suggestion 10

def main():
    N = int(input())
    for i in range(N):
        print(*[1]+[n for n in range(1,i+1) if n!=i]+[1])
main()
