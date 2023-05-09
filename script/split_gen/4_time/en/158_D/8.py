def reverse(s):
    return s[::-1]
s = input()
q = int(input())
for i in range(q):
    query = input()
    if query == '1':
        s = reverse(s)
    else:
        _, f, c = query.split()
        if f == '1':
            s = c + s
        else:
            s = s + c
print(s)
