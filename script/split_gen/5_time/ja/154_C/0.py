def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")
    return
