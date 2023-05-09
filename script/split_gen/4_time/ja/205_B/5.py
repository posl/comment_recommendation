def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print("No")
            exit()
    print("Yes")
