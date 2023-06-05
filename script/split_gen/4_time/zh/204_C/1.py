def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    count = 0
    for i in range(m):
        if a[i] != b[i]:
            count += 1
    count = count * 2 + 1
    print(count)
