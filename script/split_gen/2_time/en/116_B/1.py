def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        break
print(len(a))
You can also use a while loop to get the same result.
s = int(input())
a = [s]
while a[-1] not in a[:-1]:
    a.append(f(a[-1]))
print(len(a))
The reason why the second solution is faster is that the first solution checks the condition a[-1] in a[:-1] every time, while the second solution checks it only once.
When you use the second solution, you can also shorten the code as follows.
s = int(input())
a = [s]
while a[-1] not in a[:-1]:
    a.append(f(a[-1]))
print(len(a))
The reason why the first solution is faster is that the first solution checks the condition a[-1] in a[:-1] every time, while the second solution checks it only once.
When you use the first solution, you can also shorten the code as follows.
s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        break
print(len(a))
The reason why the second solution is faster is that the first solution checks the condition a[-1] in a[:-1] every time, while the second solution checks it only once.
When you use the second solution, you can also shorten the code as follows.
s = int(input())
a = [s]
while a[-1] not in a[:-1]:
    a.append(f(a[-1]))
print(len(a))
The reason why the first solution is faster is that the first solution checks the condition a[-1] in a[:-1] every time, while the second solution checks it only once.
When you use the first solution, you can also shorten the code as follows.
s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        break
print(len(a))
The reason why the second solution is faster is that the first solution checks the condition a[-1] in a[:-1] every
