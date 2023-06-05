def main():
    n, q = input().split()
    n = int(n)
    q = int(q)
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    for i in range(q):
        x, k = input().split()
        x = int(x)
        k = int(k)
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
                if count == k:
                    print(j+1)
                    break
        else:
            print(-1)
