def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(a[0])
        exit()
    for i in range(n-2):
        a[i+1] = a[i+1] % a[0]
        if a[i+1] == 0:
            print(a[0])
            exit()
    print(a[0])
