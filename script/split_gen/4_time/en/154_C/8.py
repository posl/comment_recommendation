def main():
    n = input()
    n = int(n)
    a = input().split()
    a = [int(m) for m in a]
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('NO')
            return
    print('YES')
