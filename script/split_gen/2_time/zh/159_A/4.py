def reverse(s):
    return s[::-1]
S = input().strip()
Q = int(input())
s = S
for i in range(Q):
    query = input().strip().split()
    if query[0] == '1':
        s = reverse(s)
    else:
        if query[1] == '1':
            s = query[2] + s
        else:
            s = s + query[2]
print(s)
