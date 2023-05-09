def main():
    n, k, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    for i in range(k):
        c = 0
        for j in range(q):
            if a[i] == l[j]:
                c += 1
        if c > q - k:
            print("Yes")
        else:
            print("No")
