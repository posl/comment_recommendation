def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(0,n):
        if i == n-1:
            print("Yes")
            break
        if a[i] == a[i+1]:
            print("No")
            break
