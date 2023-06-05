def check(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return False
    return True
n = int(input())
a = []
for i in range(n):
    s, t = input().split()
    a.append(s)
    a.append(t)

if __name__ == '__main__':
    check()