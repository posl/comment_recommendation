def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(4*n-1):
        if a[i] != a[i+1]:
            print(a[i])
            return
        else:
            i += 3
