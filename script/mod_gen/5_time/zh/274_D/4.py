def check(n, x, y, a):
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                return False
    if x in a or y in a:
        return False
    return True
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a.append(y)

if __name__ == '__main__':
    check()