def replace(s):
    s2 = ''
    for i in range(len(s)):
        if s[i] == 'a':
            s2 += 'bc'
        elif s[i] == 'b':
            s2 += 'ca'
        else:
            s2 += 'ab'
    return s2
s = input()
q = int(input())
for i in range(q):
    t, k = map(int, input().split())
    for j in range(t):
        s = replace(s)
    print(s[k - 1])

if __name__ == '__main__':
    replace()