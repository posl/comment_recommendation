Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] and s1[1] == s2[0] and s2[0] == s2[1]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] == s2[0] == s2[1] == '.':
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    if S1[0] == S1[1] == S2[0] == S2[1] == '.':
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] == s2[0] == s2[1] == "#":
        print("No")
    else:
        print("Yes")

main()

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    if S1[0] == S2[0] and S1[1] == S2[1]:
        print("Yes")
    elif S1[0] == S1[1] and S2[0] == S2[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    if (S1[0] == S1[1] == S2[0] == S2[1] == '#') or (S1[0] == S2[0] == '#') or (S1[1] == S2[1] == '#'):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def is_connected(S1, S2):
    if S1[0] == S1[1] == S2[0] == S2[1] == '.':
        return False
    if S1[0] == S1[1] == S2[0] == S2[1] == '#':
        return True
    if S1[0] == S1[1] == '.':
        return False
    if S2[0] == S2[1] == '.':
        return False
    if S1[0] == S2[0] == '.':
        return False
    if S1[1] == S2[1] == '.':
        return False
    if S1[0] == S2[0] == '#':
        return True
    if S1[1] == S2[1] == '#':
        return True
    return True

S1 = input()
S2 = input()

=======
Suggestion 9

def check(S1, S2):
    if S1[0] == S1[1] == S2[0] == S2[1] == "#":
        return "No"
    elif S1[0] == S1[1] == S2[0] == S2[1] == ".":
        return "No"
    else:
        return "Yes"

S1 = input()
S2 = input()

print(check(S1, S2))

=======
Suggestion 10

def dfs(grid, x, y):
    if grid[x][y] == 1:
        return
    grid[x][y] = 1
    if x > 0:
        dfs(grid, x-1, y)
    if y > 0:
        dfs(grid, x, y-1)
    if x < 1:
        dfs(grid, x+1, y)
    if y < 1:
        dfs(grid, x, y+1)
