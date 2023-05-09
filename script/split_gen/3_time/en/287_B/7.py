def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                print(s[i])
main()
I am trying to find the number of strings among S_1, S_2, ..., S_N whose last three characters coincide with one or more of T_1, T_2, ..., T_M.
I am getting the wrong answer for Sample Input 2 and Sample Input 3.
I have tried this code:
n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
print(count)
I am getting the correct answer for Sample Input 1.
I am not sure why I am getting the wrong answer for Sample Input 2 and Sample Input 3.
I have tried this code:
n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
print(count)
I am getting the correct answer for Sample Input 1.
I am not sure why I am getting the wrong answer for Sample Input 2 and Sample Input 3.
I have tried this code:
n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
print(count)
I am getting the correct answer for Sample Input 1.
I am not sure why I am getting the wrong answer for Sample Input 2 and Sample Input 3.
I have tried this code:
n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range
