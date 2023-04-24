Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 10
    B = 1
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = min(A, i+1)
                B = max(B, i+1)
                C = min(C, j+1)
                D = max(D, j+1)
    print(A, B)
    print(C, D)
main()

=======
Suggestion 2

def main():
    S = [input() for _ in range(10)]
    A = 10
    B = 1
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                A = min(A, i+1)
                B = max(B, i+1)
                C = min(C, j+1)
                D = max(D, j+1)
    print(A, B)
    print(C, D)

=======
Suggestion 3

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i].find('#') != -1:
            A = i + 1
            break
    for i in range(10):
        if S[9-i].find('#') != -1:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i + 1
            break
    for i in range(10):
        if S[0][9-i] == '#':
            D = 10 - i
            break
    print(A, B)
    print(C, D)

=======
Suggestion 4

def main():
    S = [input() for _ in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                A = i + 1
                break
        if A != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[9 - i][j] == "#":
                B = 10 - i
                break
        if B != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[j][i] == "#":
                C = i + 1
                break
        if C != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[j][9 - i] == "#":
                D = 10 - i
                break
        if D != 0:
            break
    print(A, B)
    print(C, D)

=======
Suggestion 5

def main():
    S = [input() for i in range(10)]
    A, B = 10, 1
    C, D = 10, 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = min(A, i)
                B = max(B, i)
                C = min(C, j)
                D = max(D, j)
    print(A + 1, B + 1)
    print(C + 1, D + 1)

=======
Suggestion 6

def main():
    S = [input() for _ in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i].count('#') > 0:
            A = i + 1
            break
    for i in range(10):
        if S[9 - i].count('#') > 0:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i + 1
            break
    for i in range(10):
        if S[0][9 - i] == '#':
            D = 10 - i
            break
    print(A, B)
    print(C, D)

=======
Suggestion 7

def main():
    s = []
    for i in range(10):
        s.append(input())

    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                a = i + 1
                break
        if a != 0:
            break

    for i in range(10):
        for j in range(10):
            if s[i][9 - j] == '#':
                b = 10 - j
                break
        if b != 0:
            break

    for i in range(10):
        for j in range(10):
            if s[j][i] == '#':
                c = i + 1
                break
        if c != 0:
            break

    for i in range(10):
        for j in range(10):
            if s[9 - j][i] == '#':
                d = 10 - j
                break
        if d != 0:
            break
    print(a, b)
    print(c, d)

main()

I have a problem with my code. I am trying to find the largest number of a list and add it to a new list. I am using the append function to add the largest number to the new list. It works fine when the list is a list of 3 numbers. But when I try to do it for a list of 10 numbers, it gives me an error. I think it is because I am using the append function to add the largest number to the new list, but I don't know how to fix it. Here is my code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = []
for i in range(10):
    new_numbers.append(max(numbers))
    numbers.remove(max(numbers))
print(new_numbers)

I'm trying to make a program that will take a list of numbers and then find the largest number in the list and then print that number. I have tried using the max function, but it doesn't work. Here is my code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(numbers))

I have a list

=======
Suggestion 8

def main():
    S = [input() for _ in range(10)]
    A = B = C = D = 0
    for i in range(10):
        if S[i].count('#') > 0:
            if A == 0:
                A = i + 1
            B = i + 1
    for i in range(10):
        if S[0][i] == '#':
            if C == 0:
                C = i + 1
            D = i + 1
    print(A, B)
    print(C, D)

=======
Suggestion 9

def main():
    S = [input() for _ in range(10)]
    A = []
    B = []
    C = []
    D = []
    for i in range(10):
        if S[i].count('#') == 10:
            A.append(i + 1)
            B.append(i + 1)
        elif S[i].count('#') == 0:
            pass
        else:
            A.append(i + 1)
            B.append(i + 1)
            for j in range(10):
                if S[i][j] == '#':
                    C.append(j + 1)
                    D.append(j + 1)
    print(min(A), max(B))
    print(min(C), max(D))

=======
Suggestion 10

def main():
    # 10 strings
    S = [input() for _ in range(10)]
    #print(S)
    # A, B, C, D
    A, B, C, D = -1, -1, -1, -1
    # A, B
    for i in range(10):
        if S[i][0] == '#':
            A = i + 1
            break
    for i in range(10):
        if S[i][9] == '#':
            B = i + 1
            break
    # C, D
    for j in range(10):
        if S[0][j] == '#':
            C = j + 1
            break
    for j in range(10):
        if S[9][j] == '#':
            D = j + 1
            break
    print(A, B)
    print(C, D)
