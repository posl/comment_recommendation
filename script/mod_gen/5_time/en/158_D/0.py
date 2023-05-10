def reverse(s):
    return s[::-1]
s = input()
q = int(input())
for i in range(q):
    t = input().split()
    if t[0] == '1':
        s = reverse(s)
    else:
        if t[1] == '1':
            s = t[2] + s
        else:
            s = s + t[2]
print(s)

if __name__ == '__main__':
    reverse()