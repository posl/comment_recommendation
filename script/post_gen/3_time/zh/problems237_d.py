Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    #print(n,s)
    a = [0]
    for i in range(1,n+1):
        if s[i-1] == 'L':
            a.insert(0,i)
        else:
            a.append(i)
    print(*a)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = [0] * (n + 1)
    l = 0
    r = n
    for i in range(n):
        if s[i] == 'L':
            ans[l] = i + 1
            l += 1
        else:
            ans[r] = i + 1
            r -= 1
    print(*ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(' '.join(map(str, a)))
    return

=======
Suggestion 4

def solve():
    n = int(input())
    s = input()
    l = 0
    r = 0
    ans = [0]
    for i in range(n):
        if s[i] == 'L':
            l += 1
            ans.insert(r, i + 1)
        else:
            r += 1
            ans.append(i + 1)
    print(' '.join(map(str, ans)))

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = [0] * (n+1)
    left = 0
    right = n
    for i in range(n):
        if s[i] == 'L':
            ans[right] = i+1
            right -= 1
        else:
            ans[left] = i+1
            left += 1
    print(*ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n-1):
        if s[i] == 'R':
            a.append(i+1)
        else:
            a.insert(0,i+1)
    print(*a)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    l = 0
    r = n
    ans = [0] * (n+1)
    for i in range(n):
        if s[i] == 'L':
            r -= 1
            ans[r] = i + 1
        else:
            l += 1
            ans[l] = i + 1
    print(' '.join(map(str,ans[l:r])))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    l = 0
    r = n
    for i in range(n):
        if s[i] == 'L':
            r -= 1
        else:
            l += 1
    for i in range(l):
        print(i+1, end=' ')
    for i in range(r):
        print(l+r-i, end=' ')
    print()

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1, n):
        if s[i - 1] == 'L':
            a.insert(0, i)
        else:
            a.append(i)
    a = list(map(lambda x: str(x), a))
    print(' '.join(a))

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0,i+1)
        else:
            a.append(i+1)
    print(*a)
