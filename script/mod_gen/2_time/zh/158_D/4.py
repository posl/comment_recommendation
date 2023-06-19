def reverse(s):
    return s[::-1]
s = input()
q = int(input())
for i in range(q):
    t = input().split()
    if t[0] == '1':
        s = reverse(s)
    else:
        f = int(t[1])
        c = t[2]
        if f == 1:
            s = c + s
        else:
            s = s + c
print(s)

if __name__ == '__main__':
    reverse()