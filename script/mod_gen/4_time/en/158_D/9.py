def reverse(s):
    return s[::-1]
s = input()
q = int(input())
rev = False
head = ""
tail = ""
for i in range(q):
    t = input().split()
    if t[0] == "1":
        rev = not rev
    else:
        if t[1] == "1":
            if rev:
                tail += t[2]
            else:
                head += t[2]
        else:
            if rev:
                head += t[2]
            else:
                tail += t[2]

if __name__ == '__main__':
    reverse()