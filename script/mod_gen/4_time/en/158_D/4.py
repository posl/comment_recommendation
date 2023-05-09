def reverse(s):
    return s[::-1]
s = input()
q = int(input())
for i in range(q):
    query = input().split()
    if int(query[0]) == 1:
        s = reverse(s)
    else:
        if int(query[1]) == 1:
            s = query[2] + s
        else:
            s = s + query[2]
print(s)

if __name__ == '__main__':
    reverse()