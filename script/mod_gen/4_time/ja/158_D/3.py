def reverse(s):
    return s[::-1]
s = input()
q = int(input())
head = ''
tail = ''
for i in range(q):
    query = input().split()
    if query[0] == '1':
        head, tail = tail, head
    else:
        if query[1] == '1':
            head = query[2] + head
        else:
            tail += query[2]
print(reverse(head) + s + tail)
