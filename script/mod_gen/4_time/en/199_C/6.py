def swap(s, a, b):
    a -= 1
    b -= 1
    if a < len(s)/2 and b < len(s)/2:
        s[a], s[b] = s[b], s[a]
    elif a >= len(s)/2 and b >= len(s)/2:
        s[a], s[b] = s[b], s[a]
    else:
        if a >= len(s)/2:
            a -= len(s)/2
            b += len(s)/2
        else:
            a += len(s)/2
            b -= len(s)/2
        s[a], s[b] = s[b], s[a]
    return s
n = input()
s = list(raw_input())
q = input()
for i in xrange(q):
    t, a, b = map(int, raw_input().split())
    if t == 1:
        s = swap(s, a, b)
    else:
        s[:n], s[n:] = s[n:], s[:n]
print "".join(s)

if __name__ == '__main__':
    swap()