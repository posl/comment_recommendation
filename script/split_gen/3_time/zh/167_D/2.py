def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    for i in range(k):
        a[i] = a[i] - 1
    for i in range(n):
        if i == 0:
            b = [a[i]]
        else:
            b.append(a[b[i-1]])
        if b[i] == 0:
            print(i+1)
            return
    print(b[k] + 1)
