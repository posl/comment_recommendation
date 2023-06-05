def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    k = 0
    for i in range(n):
        if i != 0 and a[i] != a[i-1]:
            k += 1
        print(k)
