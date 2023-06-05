def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        if i + 1 != a[i]:
            print("No")
            exit()
    print("Yes")
