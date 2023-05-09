def find(a, b):
    if a == b:
        return a
    if a > b:
        return find(a//2, b)
    else:
        return find(a, b//2)
n = int(input())
d = dict()
for i in range(n):
    l, *a = map(int, input().split())
    a.sort()
    a = tuple(a)
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
count = 0
for v in d.values():
    count += v * (v-1) // 2
print(count)
I don't know why this code is not working. I'm getting 0 as output. Please help me.
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list of lists. I want to convert it into a dictionary. I have tried using dict() but it doesn't work. Please help me.
How do you convert a list of lists into a dictionary?
I have a list
