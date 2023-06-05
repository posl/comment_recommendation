def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(1, n):
        if a[i - 1] == a[i]:
            print("NO")
            break
    else:
        print("YES")
