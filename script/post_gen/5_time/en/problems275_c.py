Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = []
    for i in range(9):
        s.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 2

def main():
    s = []
    for i in range(9):
        s.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    count = 0
    for i in range(9):
        s = input()
        for j in range(9):
            if s[j] == '#':
                count += 1
    print(count)

=======
Suggestion 4

def main():
    str_list = []
    for i in range(9):
        str_list.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if str_list[i][j] == '#':
                count += 1

    print(count)

=======
Suggestion 5

def main():
    str = []
    for i in range(9):
        str.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if str[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 6

def main():
    s = []
    for i in range(9):
        s.append(input())
    p = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                p += 1
    print(p)

=======
Suggestion 7

def get_input():
    input_list = []
    for i in range(9):
        input_list.append(input())
    return input_list

=======
Suggestion 8

def check(r, c):
    if s[r][c] == '#':
        return True
    else:
        return False

s = []
for _ in range(9):
    s.append(input())

ans = 0
for i in range(9):
    for j in range(9):
        if i == 0 or i == 8:
            if j == 0 or j == 8:
                if check(i, j):
                    ans += 1
            else:
                if check(i, j) and check(i, j+1):
                    ans += 1
        else:
            if j == 0 or j == 8:
                if check(i, j) and check(i+1, j):
                    ans += 1
            else:
                if check(i, j) and check(i, j+1) and check(i+1, j) and check(i+1, j+1):
                    ans += 1

print(ans)

=======
Suggestion 9

def check_pawn(S, r, c):
    if S[r][c] == '#':
        return True
    else:
        return False

=======
Suggestion 10

def main():
    #get input
    input = []
    for i in range(9):
        input.append(list(input()))

    #initialize count
    count = 0

    #count
    for i in range(9):
        for j in range(9):
            if i + 1 < 9 and j + 1 < 9:
                if input[i][j] == '#' and input[i+1][j] == '#' and input[i][j+1] == '#' and input[i+1][j+1] == '#':
                    count += 1

    #print
    print(count)

main()
