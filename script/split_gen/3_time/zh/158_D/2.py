def reverse(s):
    return s[::-1]
s = input()
q = int(input())
for i in range(q):
    query = input().split()
    if query[0] == '1':
        s = reverse(s)
    elif query[0] == '2':
        if query[1] == '1':
            s = query[2] + s
        elif query[1] == '2':
            s = s + query[2]
print(s)
