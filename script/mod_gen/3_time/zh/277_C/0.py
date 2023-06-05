def check(a, b):
    if a == b:
        return True
    elif a > b:
        return False
    else:
        return True
n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])
l.sort(key=lambda x: x[1])
ans = 1
for i in range(n):
    if check(ans, l[i][0]):
        ans = l[i][1]
    else:
        pass
print(ans)

if __name__ == '__main__':
    check()