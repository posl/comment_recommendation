Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        break
print(i)

=======
Suggestion 2

def main():
    num = int(input())
    list = []
    list.append(num)
    while True:
        if num % 2 == 0:
            num = num / 2
            list.append(int(num))
        else:
            num = 3 * num + 1
            list.append(int(num))
        if list.count(num) == 2:
            break
    print(len(list))

=======
Suggestion 3

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

=======
Suggestion 4

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[s]
for i in range(1,1000000):
    a.append(f(a[i-1]))
    if a[i]==a[i-2]:
        print(i+1)
        break

=======
Suggestion 5

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(raw_input())
a=[s]
i=1
while True:
    a.append(f(a[i-1]))
    if a[i] in a[:i]:
        print i+1
        break
    i+=1

=======
Suggestion 6

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[s]
while True:
    s=f(s)
    if s in a:
        print(len(a)+1)
        break
    else:
        a.append(s)

=======
Suggestion 7

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1]%2 == 0:
            a.append(a[-1]//2)
        else:
            a.append(3*a[-1]+1)
        if a.count(a[-1]) == 2:
            break
    print(len(a)-1)

=======
Suggestion 8

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1] % 2 == 0:
            a.append(a[-1] // 2)
        else:
            a.append(3 * a[-1] + 1)
        if a[-1] in a[:-1]:
            print(len(a))
            break
