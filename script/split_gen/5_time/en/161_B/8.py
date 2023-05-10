def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total * 1/(4*m):
            print("No")
            return
    print("Yes")
