def check(a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] == 'L':
                continue
            if a[i][j] == 'L' and a[j][i] == 'W':
                continue
            if a[i][j] == 'D' and a[j][i] == 'D':
                continue
            return False
    return True
n = int(input())
a = [list(input()) for _ in range(n)]
print('correct' if check(a) else 'incorrect')
The solution is based on the observation that if the given table is not contradictory, then:
Player i beat Player j, if and only if Player j lost to Player i;
Player i lost to Player j, if and only if Player j beat Player i;
Player i drew with Player j, if and only if Player j drew with Player i.
So, the solution is to check if the above conditions hold for all i and j.
The solution is written in Python 3.6.5.
import sys
input = sys.stdin.readline
n = int(input())
a = [input() for _ in range(n)]
ans = 'correct'
for i in range(n):
    for j in range(n):
        if i == j:
            if a[i][j] != '-':
                ans = 'incorrect'
        else:
            if a[i][j] == 'W' and a[j][i] != 'L':
                ans = 'incorrect'
            if a[i][j] == 'L' and a[j][i] != 'W':
                ans = 'incorrect'
            if a[i][j] == 'D' and a[j][i] != 'D':
                ans = 'incorrect'
print(ans)
The solution is based on the observation that if the given table is not contradictory, then:
Player i beat Player j, if and only if Player j lost to Player i;
Player i lost to Player j, if and only if Player j beat Player i;
Player i drew with Player j, if and only if Player j drew with Player i.
So, the solution is to check if the above conditions hold for all i and j.
The solution is written in Python 3.6.5.

if __name__ == '__main__':
    check()