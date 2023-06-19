def cmp(a,b):
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                if a[i] < b[i]:
                    return -1
                else:
                    return 1
        return 0
    elif len(a) < len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                if a[i] < b[i]:
                    return -1
                else:
                    return 1
        return -1
    else:
        for i in range(len(b)):
            if a[i] != b[i]:
                if a[i] < b[i]:
                    return -1
                else:
                    return 1
        return 1
x = input()
n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort(key=lambda x:cmp(x,x.lower()))
print('\n'.join(s))

if __name__ == '__main__':
    cmp()