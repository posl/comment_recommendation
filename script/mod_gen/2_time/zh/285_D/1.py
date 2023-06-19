def is_ok(i):
    if i == 0:
        return True
    if s[i] == t[i-1]:
        return True
    else:
        return False
n = int(input())
s = []
t = []
for i in range(n):
    s1, t1 = input().split()
    s.append(s1)
    t.append(t1)
for i in range(n):
    if is_ok(i):
        continue
    else:
        print('No')
        break
else:
    print('Yes')

if __name__ == '__main__':
    is_ok()