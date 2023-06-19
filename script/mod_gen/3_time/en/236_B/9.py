def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    for i in range(1,4*n - 1):
        if a[i] == a[i-1]:
            count += 1
        else:
            count = 0
        if count == 3:
            print(a[i])
            break
main()
