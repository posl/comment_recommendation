def main():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    if n%2 == 0:
        print("No")
        return
    if n == 1:
        print("Yes")
        return
    if n == 2:
        print("No")
        return
    for i in range(n-1):
        if a[i] != 1 and b[i] != 1:
            print("No")
            return
    print("Yes")
