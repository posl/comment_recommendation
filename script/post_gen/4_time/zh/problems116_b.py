Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1]%2 == 0:
            a.append(a[-1]//2)
        else:
            a.append(a[-1]*3+1)
        if a.count(a[-1]) == 2:
            break
    print(len(a)-1)
main()

=======
Suggestion 2

def f(n):
	if n%2 == 0:
		return n/2
	else:
		return 3*n+1

=======
Suggestion 3

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

=======
Suggestion 4

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[s]
m=1
while True:
    m+=1
    a.append(f(a[m-2]))
    if a[m-1] in a[0:m-1]:
        break
print(m)

=======
Suggestion 5

def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(f(a[i-2]))
    if a.count(a[i-1]) == 2:
        break
print(i)
